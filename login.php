<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <link rel="stylesheet" href="login.css"> <!-- Link to your CSS file -->
</head>
<body>
  <div class="nav-container">
    <header>
      <div class="logo">ArconHUB</div>
      <nav>
        <a href="index.php">Home</a>
      </nav>
      <button class="login-signup" onclick="location.href='login.php'">Login / Sign In</button>
    </header>
  </div>

  <div class="container">
    <div class="login-form-container">
      <h2>Login</h2>
      <form class="login-form" action="process_login.php" method="POST"> <!-- Action added for form submission -->
        <input type="email" name="email" placeholder="Email" required />
        <input type="password" name="password" placeholder="Password" required />
        <button type="submit" class="login-button">Log In</button>
      </form>
      <div class="login-links">
        <a href="forgot_password.php">Forgot Password?</a>
        <a href="signup.php">Sign Up</a>
      </div>
    </div>
  </div>
  
</body>
</html>
