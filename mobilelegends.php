<?php
// process_recharge.php

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user_id = $_POST['user_id'] ?? null;
    $server = $_POST['server'] ?? null;
    $diamond_pack = $_POST['diamond_pack'] ?? null;

    if ($user_id && $server && $diamond_pack) {
        // Simulate recharge process (in a real scenario, add actual logic)
        echo "<h2>Recharge Successful!</h2>";
        echo "<p>User ID: $user_id</p>";
        echo "<p>Server: $server</p>";
        echo "<p>Diamond Pack: $diamond_pack Diamonds</p>";
        echo '<a href="index.php">Go Back</a>';
    } else {
        echo "<p>Invalid input. Please try again.</p>";
    }
}
?>
