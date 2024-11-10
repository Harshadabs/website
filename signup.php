<?php
// login.php

session_start();

$valid_email = "user@example.com"; // Replace with database or actual data in production
$valid_password = "password123";   // Replace with hashed password for real-world usage

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $email = $_POST['email'] ?? '';
    $password = $_POST['password'] ?? '';

    if ($email === $valid_email && $password === $valid_password) {
        // Successful login
        $_SESSION['user'] = $email;
        header("Location: index.php"); // Redirect to main page after login
        exit;
    } else {
        // Failed login
        $error_message = "Invalid email or password. Please try again.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <link rel="stylesheet" href="login.css">
</head>
<body>
  <div class="container">
    <div class="login-form-container">
      <h2>Login</h2>
      <?php if (!empty($error_message)) : ?>
        <p style="color: red;"><?php echo $error_message; ?></p>
      <?php endif; ?>
      <form class="login-form" action="login.php" method="POST">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" class="login-button">Log In</button>
      </form>
      <div class="login-links">
        <a href="#">Forgot Password?</a>
        <a href="signup.php">Sign Up</a>
      </div>
    </div>
  </div>
</body>
</html>
