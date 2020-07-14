SummerProject2

An Android app for downloading fanfiction from various sites and sending them directly to a Kindle device written in Python using [Kivy](https://kivy.org/). The backend uses [FanFicFare](https://github.com/JimmXinu/FanFicFare) and fiction from any site supported by FanFicFare can be downloaed. In order to use, create a file named password.py with the following contents and add it to the src directory. 

```python
my_email = ""
#email to send the mobi file using
password = ""
#password to that email (may be an app password)
kindle_email = ""
#email to send the file to, doesn't have to be a kindle email
```
To build and install the app run `buildozer -v android debug` to compile and `buildozer android deploy run` to deploy the app. View [Buildozer](https://buildozer.readthedocs.io/en/latest/) for more detailed instruction.
