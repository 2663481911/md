## 导入

```groovy
implementation 'com.github.bumptech.glide:glide:4.11.0'
annotationProcessor 'com.github.bumptech.glide:compiler:4.11.0'
```

## 加载图片

```kotlin
Glide.with(context)
     .load(url)
     .into(imageView);
```

- with(Context context) - conten：上下文

- url ：网络图片地址
- imageView ：显示图片的目标 ImageView