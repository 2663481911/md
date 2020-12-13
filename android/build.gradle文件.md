## bulid.gradle文件

### 最外层的bulid.gradle文件

```groovy
buildscript {
    ext.kotlin_version = "1.3.72"
    repositories {
        // 代码仓库，声明后可以使用其中的依赖库
        google()
        jcenter()
    }
    dependencies {
        // 声明gradle插件，用于构建Android项目
        classpath "com.android.tools.build:gradle:4.0.1"
        // kotlin插件，表明当前项目是由kotlin进行开发的
        classpath "org.jetbrains.kotlin:kotlin-gradle-plugin:$kotlin_version"
    }
}

allprojects {
    repositories {
        google()
        jcenter()
    }
}

```

### app目录下的bulid.gradle文件

```groovy
apply plugin: 'com.android.application'   // 表示这是一个应用程序模块
apply plugin: 'kotlin-android'   // 使用kotlin开发android项目
apply plugin: 'kotlin-android-extensions'    // kotlin扩展功能

android {
    compileSdkVersion 29    // 项目编译的版本，这里是Android 10.0系统的SDK编译
    buildToolsVersion "30.0.1"    // 项目构建工具的版本

    defaultConfig {
        // 每个应用的唯一标识，不能重复。默认是包名
        applicationId "com.example.myapplication"   
        minSdkVersion 21    // 项目最低兼容的Android版本，这里是5.0
        targetSdkVersion 29
        versionCode 1    // 指定项目的版本号
        versionName "1.0"    // 指定项目的版本名

        testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            
            minifyEnabled false   // 是否对项目的代码进行混淆
            // 混淆时的规则文件
            proguardFiles getDefaultProguardFile('proguard-android-optimize.txt'), 'proguard-rules.pro'
        }
    }
}

// 指定当前项目的依赖关系
dependencies {
    // 本地依赖声明，表示将libs目录下的所有.jar后缀的文件添加到项目的构建路径中。
    implementation fileTree(dir: "libs", include: ["*.jar"])
    // 远程依赖声明
    implementation "org.jetbrains.kotlin:kotlin-stdlib:$kotlin_version"
    implementation 'androidx.core:core-ktx:1.3.1'
    implementation 'androidx.appcompat:appcompat:1.2.0'
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'
    testImplementation 'junit:junit:4.12'
    androidTestImplementation 'androidx.test.ext:junit:1.1.1'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.2.0'

}
```

- 第一行有两种选择：
  - **'com.android.application' **  :表示这是一个应用程序模块，可以直接运行
  - **'com.android.library'** ：表示这是一个库模块，要依赖于别的应用模块运行

