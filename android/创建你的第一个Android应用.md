### AndroidManifest.xml

```xml
<activity android:name=".MainActivity">
    <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
    </intent-filter>
</activity>
```

- 这段代码表示对MainActivity进行注册，没有在**AndroidManifest.xml**里注册的Activity是不能使用的。
- 其中**intent-filter**里的

```xml
<action android:name="android.intent.action.MAIN" />
<category android:name="android.intent.category.LAUNCHER" />
```

- 表示这个项目的**主Activity**，在手机上点击应用图标，首先启动的就是这个Activity。

### MainActivity.kt

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```

- **MainActivity**继承自AppCompatActivity。AppCompatActivity是AndroidX中提供的一种向下兼容的Activity。
- 在**MainActivity**中有一个**onCreate()**方法，这个方法是一个**Activity被创建**时要执行的方法。

- 在**onCreate()**方法调用了**setContentView()**方法，这个方法给当前的Activity加载**activity_main**布局。

### Android应用的启动

1. 读取**AndroidManifest.xml**文件，找到**主Activity**，启动Activity加载布局。