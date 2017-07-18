<!DOCTYPE html>
<html>
  <head>
    <title>Workshop - Testprojekt</title>
  </head>
  <body>
    <form action="#" method="POST">
    <input type="text" name="user">
    <br>
    <input type="password" name="pass">
    <br>
    <button type="submit" name="Submit">Submit</button>
  </form>

  <?php
    if ( isset( $_POST ) )
    {
      if ( $_POST["user"] == "me" && $_POST["pass"] == "pass" )
      {
        echo "Success";
      }
      else
      {
        echo "Fail";
      }
    }
  ?>
  </body>
</html>
