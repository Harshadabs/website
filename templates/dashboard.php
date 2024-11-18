<?php
session_start();

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
    header("Location: login.php"); // Redirect to login page if not logged in
    exit();
}

// User is logged in, display dashboard
echo "Welcome, " . $_SESSION['username'] . "!";
?>
