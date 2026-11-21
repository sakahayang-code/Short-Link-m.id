<?php
/**
 * Short Link m.id - Live 302 Redirection Engine for cPanel / PHP Apache
 * Compatible with multimediatama.com and m.id
 */

// Prevent caching so click counts & destinations are always fresh
header("Cache-Control: no-cache, no-store, must-revalidate");
header("Pragma: no-cache");
header("Expires: 0");

// Get alias from query or path
$alias = isset($_GET['alias']) ? trim($_GET['alias']) : '';

if (empty($alias) && isset($_SERVER['REQUEST_URI'])) {
    $parsedUri = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
    $segments = array_filter(explode('/', trim($parsedUri, '/')));
    $alias = end($segments);
}

// Clean alias
$alias = strtolower(preg_replace('/[^a-zA-Z0-9_\-]/', '', $alias));

$dataFile = __DIR__ . '/links.json';
$links = [];

if (file_exists($dataFile)) {
    $json = file_get_contents($dataFile);
    $links = json_decode($json, true) ?: [];
}

// Default fallback links if links.json is missing
if (empty($links)) {
    $links = [
        "custom" => [
            "alias" => "custom",
            "long_url" => "https://shopee.co.id/toko-kopi-nusantara/promo-spesial-diskon-50",
            "clicks" => 148
        ],
        "promo" => [
            "alias" => "promo",
            "long_url" => "https://google.com",
            "clicks" => 42
        ],
        "wa-pesan" => [
            "alias" => "wa-pesan",
            "long_url" => "https://wa.me/628123456789",
            "clicks" => 12480
        ]
    ];
}

// Check if alias exists in database
if (!empty($alias) && isset($links[$alias])) {
    // Increment click count
    $links[$alias]['clicks'] = ($links[$alias]['clicks'] ?? 0) + 1;
    if (is_writable($dataFile)) {
        @file_put_contents($dataFile, json_encode($links, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES));
    }

    $target = $links[$alias]['long_url'];
    // Ensure URL has protocol
    if (!preg_match('~^(?:f|ht)tps?://~i', $target)) {
        $target = "https://" . $target;
    }

    // Execute 302 Found Redirect to original target link
    header("Location: " . $target, true, 302);
    exit;
}

// Fallback to home page if alias not recognized
header("Location: index.html?not_found=" . urlencode($alias), true, 302);
exit;
