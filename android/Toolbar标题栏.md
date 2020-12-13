### 默认的ActionBar如何来的

- 根据项目中指定的主题来显示
- 打开AndroidManifest.xml文件，其中有

```
android:theme="@style/AppTheme"
```

- 这里使用了AppTheme的主题，是在res/values文件夹下的styles.xml文件里的

```xml
<resources>
    <!-- Base application theme. -->
    <style name="AppTheme" parent="Theme.AppCompat.Light.ActionBar">
        <!-- Customize your theme here. -->
        <item name="colorPrimary">@color/colorPrimary</item>
        <item name="colorPrimaryDark">@color/colorPrimaryDark</item>
        <item name="colorAccent">@color/colorAccent</item>
    </style>
</resources>
```

-  其中**name="AppTheme" parent="Theme.AppCompat.Light.ActionBar"** 就是指定一个主题，项目中的ActionBar主题就是这个

### 不使用ActionBar

- 修改**styles.xml**文件，指定一个不带**ActionBar**的主题，就可以使用**Toolbar**了

```xml
<style name="AppTheme" parent="Theme.AppCompat.Light.NoActionBar">
```

### 使用Toolbar

- 在**activity_main.xml**文件中添加

```xml
<androidx.appcompat.widget.Toolbar
    android:id="@+id/toolbar"
    android:layout_width="match_parent"
    android:background="@color/colorPrimary"
    android:layout_height="?attr/actionBarSize"/>
```

- 修改**MainActivity**文件，设置toolbar标题栏

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    setContentView(R.layout.activity_main)
    setSupportActionBar(toolbar)
```



### 添加菜单选项

#### 自定义的菜单选项：**R.menu.toolbar**

```xml
<?xml version="1.0" encoding="utf-8"?>
<menu xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto">
    <item
        android:id="@+id/edit_rule"
        android:icon="@drawable/edit"
        app:showAsAction="ifRoom"
        android:title="@string/edit_rule">
    </item>

    <item
        android:id="@+id/remove_rule"
        android:icon="@drawable/remove"
        app:showAsAction="ifRoom"
        android:title="@string/remove_rule"/>
</menu>
```
- **app:showAsAction="(参数)"**：
  - **always**：总是显示在界面上
  - **never**：不显示在界面上，只让出现在右边的三个点中
  - **ifRoom**：如果有位置才显示，不然就出现在右边的三个点中

#### 在activity文件中重写**onCreateOptionsMenu**方法，添加菜单

```kotlin
override fun onCreateOptionsMenu(menu: Menu?): Boolean {
    menuInflater.inflate(R.menu.toolbar, menu)
    return true
}
```

#### 添加点击事件，重写**onOptionsItemSelected**方法

```kotlin
// 导航栏按钮功能
    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        when(item.itemId){
            R.id.edit_rule -> {
                // 点击事件
            }
            R.id.add_rule -> {
            }
        }
        return true
    }
```

### 一些主题



