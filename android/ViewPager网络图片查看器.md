## BigViewPagerAdapter

```kotlin

class BigViewPagerAdapter(val viewLists:ArrayList<View>, val imgUrlList:ArrayList<String>) : PagerAdapter() {

    override fun getCount(): Int {
        return viewLists.size
    }
	//View 是否和 Object有关联关系
    override fun isViewFromObject(view: View, `object`: Any): Boolean {
        return view == `object`
    }
	//  初始化一个item数据的时候的回调
    override fun instantiateItem(container: ViewGroup, position: Int): Any {
        container.addView(viewLists[position]);
        // 加载图片
        Glide.with(container)
            .load(imgUrlList[position])
            .into(viewLists[position].big_img_view)
        return viewLists[position];
    }
	// 销毁一个item数据的时候会回调
    override fun destroyItem(container: ViewGroup, position: Int, `object`: Any) {
        container.removeView(viewLists[position]);
    }
}
```

## ShowBigImgActivity

```kotlin
class ShowBigImgActivity : AppCompatActivity() {
    private var aList: ArrayList<View>? = null
    private val mAdapter: BigViewPagerAdapter? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_show_big_img)

        // 网络图片地址列表
        val imgUrlList = intent.getStringArrayListExtra("imgList") as ArrayList<String>
        // 获取点击图片位置
        val position = intent.getIntExtra("position", 0)
        aList = ArrayList<View>()
        // 添加view
        for(imgUrl in imgUrlList){
            aList!!.add(
                layoutInflater.inflate(R.layout.show_big_img, null, false))
        }

        show_big_viewPager.adapter = BigViewPagerAdapter(aList!!, imgUrlList)
        show_big_viewPager.currentItem = position   // 显示点击的图片
    }
}
```

## show_big_view.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical" android:layout_width="match_parent"
    android:layout_height="match_parent">

    <ImageView
        android:id="@+id/big_img_view"
        android:src="@drawable/load"
        android:background="#555F71"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>
</LinearLayout>
```

## activity_show_big_img.xml



```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".ShowBigImgActivity">
    <androidx.viewpager.widget.ViewPager
        android:id="@+id/show_big_viewPager"
        android:layout_width="match_parent"
        android:layout_height="match_parent"/>

</androidx.constraintlayout.widget.ConstraintLayout>
```

