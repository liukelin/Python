# selenium 的一些运用

==== 百度贴吧自动登录、签到 ====

环境: python3

依赖库: pip install selenium , requests

运行脚本: tieba.py 

使用的接口为无验证码接口，有验证码的话请自行实现。

登录过程使用selenium webdriver操作并获取登录cookie，签到过程为请求签到接口


# 资源下载

自动化web测试工具 seleniumhq下载
http://www.seleniumhq.org/download/

firefox驱动下载
https://github.com/mozilla/geckodriver/releases

google chrome驱动
https://sites.google.com/a/chromium.org/chromedriver/downloads
https://chromedriver.storage.googleapis.com/index.html

mac环境配置
http://www.cnblogs.com/liuqing0328/p/5914074.html

无显示器服务器使用Xvfb 来运行Selenium2 
http://www.tuicool.com/articles/7jUFr2V

无GUI的server上通过虚拟显示来运行Selenium2 (webdriver)
pyvirtualdisplay包 依赖于Xvfb