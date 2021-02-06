### RecyclerView底部刷新

- 在初始化时不把数据传进去，自定义一个**setData**传数据

```kotlin

class ImgIndexAdapter(val context: Context,private val curRuleNum: Int) :
    RecyclerView.Adapter<ImgIndexAdapter.ViewHolder>(){
    private var imgList: List<ImgIndex> = ArrayList()

    fun setData(imgList: List<ImgIndex>) {
        // 传入数据
        this.imgList = imgList
        // 更新页面
        notifyItemRangeChanged(0, imgList.size)
    }

    inner class ViewHolder(view: View):RecyclerView.ViewHolder(view){
        // 获取控件
        val indexImg:ImageView = view.findViewById(R.id.imageIndex_img)
        val indexName:TextView = view.findViewById(R.id.imageIndex_name)

    }


    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        // 添加控件位置
        val view = LayoutInflater.from(context)
            .inflate(R.layout.img_index_item, parent, false)
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        // 向控件中添加数据
        val imgIndex = imgList[position]
        if (imgIndex.imgId != 0) holder.indexImg.setImageResource(imgIndex.imgId)
        else Glide.with(holder.itemView)
            .load(imgIndex.imgSrc)
            .centerCrop()
            .placeholder(R.drawable.load)
            .dontAnimate()
            .into(holder.indexImg)

        holder.indexName.text = imgIndex.name
    }

    // 数据长度
    override fun getItemCount() = imgList.size
}


```

#### mainActivity

- 获取数据，添加到**Adapter**中

```kotlin
private val imgList = ArrayList<ImgIndex>()
imgList.add(ImgIndex(img_url.title, img_url.href, img_url.src))
adapter.setData(imgList)
```

