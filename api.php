<?php
/**
 * REST API for Short Link m.id (cPanel & PHP Compatible)
 */

header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: GET, POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type, Authorization, X-Requested-With");

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    http_response_code(200);
    exit;
}

$dataFile = __DIR__ . '/links.json';

function getLinks($file) {
    if (file_exists($file)) {
        $json = file_get_contents($file);
        return json_decode($json, true) ?: [];
    }
    return [];
}

function saveLinks($file, $links) {
    return file_put_contents($file, json_encode($links, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
}

$action = isset($_GET['action']) ? $_GET['action'] : '';

// Also check path if action not in query
if (empty($action) && isset($_SERVER['REQUEST_URI'])) {
    $path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
    if (strpos($path, 'shorten') !== false) $action = 'shorten';
    elseif (strpos($path, 'click') !== false) $action = 'click';
    elseif (strpos($path, 'links') !== false) $action = 'links';
}

$input = json_decode(file_get_contents("php://input"), true) ?: $_POST;

switch ($action) {
    case 'shorten':
        $longUrl = isset($input['long_url']) ? trim($input['long_url']) : '';
        $alias = isset($input['alias']) ? trim($input['alias']) : '';

        if (empty($longUrl)) {
            http_response_code(400);
            echo json_encode(["success" => false, "error" => "URL cannot be empty"]);
            exit;
        }

        // Clean alias
        $alias = preg_replace('~^https?://[^/]+/~', '', $alias);
        $alias = strtolower(preg_replace('/[^a-zA-Z0-9_\-]/', '', $alias));
        if (empty($alias)) {
            $alias = "custom";
        }

        if (!preg_match('~^(?:f|ht)tps?://~i', $longUrl)) {
            $longUrl = "https://" . $longUrl;
        }

        $links = getLinks($dataFile);
        $links[$alias] = [
            "alias" => $alias,
            "long_url" => $longUrl,
            "clicks" => isset($links[$alias]['clicks']) ? $links[$alias]['clicks'] : 0,
            "created_at" => date("Y-m-d H:i:s")
        ];
        saveLinks($dataFile, $links);

        $host = isset($_SERVER['HTTP_HOST']) ? $_SERVER['HTTP_HOST'] : 'multimediatama.com';
        echo json_encode([
            "success" => true,
            "alias" => $alias,
            "long_url" => $longUrl,
            "short_url" => "https://m.id/" . $alias,
            "hosting_url" => "https://" . $host . "/" . $alias,
            "clicks" => $links[$alias]['clicks']
        ]);
        break;

    case 'click':
        $alias = isset($input['alias']) ? strtolower(trim($input['alias'])) : '';
        $links = getLinks($dataFile);
        if (!empty($alias) && isset($links[$alias])) {
            $links[$alias]['clicks'] = ($links[$alias]['clicks'] ?? 0) + 1;
            saveLinks($dataFile, $links);
            echo json_encode(["success" => true, "clicks" => $links[$alias]['clicks']]);
        } else {
            http_response_code(404);
            echo json_encode(["success" => false, "error" => "Link not found"]);
        }
        break;

    case 'links':
    default:
        $links = getLinks($dataFile);
        echo json_encode($links);
        break;
}
