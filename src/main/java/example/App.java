package example;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.setProperty("webdriver.chrome.driver",
                "C:\\Users\\kanis\\Documents\\Legit Stuff\\NUS\\YSI SEA\\Java Extras\\chromedriver_win32\\chromedriver.exe");
        ChromeOptions options = new ChromeOptions();
//        options.addArguments("--headless");
        options.addArguments("--start-maximized");
        options.addArguments("--window-size=1920x1080");
        WebDriver driver = new ChromeDriver(options);
        String url = "https://shopee.sg/HYDRAULIC-MONITOR-MOUNTING-ARM-NB-F80-LCD-SCREEN-DESK-TABLE-VESA-MOUNT-STAND-360-ADJUSTABLE-ROTATION-i.13842071.2689454006";
        driver.get(url);

        WebElement title = driver.findElement(By.xpath("//span[contains(text(), 'VESA MOUNT')]"));
        System.out.println(title.getText());

        WebElement product = driver.findElement(By.xpath("//button[contains(text(), 'F80')]"));
        product.click();

        WebElement price = driver.findElement(By.xpath("//div[@class='_3e_UQT']"));
        System.out.println(price.getText());
    }
}
