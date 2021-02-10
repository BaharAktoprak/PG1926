<html>
    <head>

    </head>
    <?php
    if($_POST)
    {
      $s1=$_POST["sayi"];
      $sayac=0;
      for($i=1; $i<=$s1;$i++)
      {
        if(($s1% $i)==0)
        {
          $sayac++;
        }
        if($sayac>2)
        {
            $mesaj=$s1. " "."sayısı asal bir sayı değildir.";
        }
        if($sayac<=2)
        {
            $mesaj=$s1. " "."sayısı asal bir sayıdır.";

        }
      }
      echo $mesaj;
    }
    ?>
    <body>

        <form name="AsalSayi" action="asal.php" method="post">
            <input type="text" name="sayi"> <br> <br>
            <input type="submit" value="Asal Sayı mı?">
        </form>
    </body>
</html>
