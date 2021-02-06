package singleton;

public class Singleton {

    public static void main(String[] args) {
        Singleton01 s1 = Singleton01.getInstance();
        Singleton01 s2 = Singleton01.getInstance();
        System.out.println(s1 == s2);
    }
}


/**
 * 饿汉式 类加载到内存后，就实例化一个单例，JVM保证线程安全 
 * 简单实用，推荐实用; 
 * 唯一缺点: 不管用到与否，类加载时就完成实例化
 * 
 */
class Singleton01 {
    private static final Singleton01 INSTANCE = new Singleton01();

    private Singleton01() {
    };

    public static Singleton01 getInstance() {
        return INSTANCE;
    }

}

/**
 * lazy loading 懒汉式 
 * 用的时候初始化 线程不安全
 */
class Singleton02 {
    
    private Singleton02() {
    }
    // private static Singleton02 INSTANCE;
    // public static Singleton02 getInstance() {
    //     if (INSTANCE == null) {
    //         INSTANCE = new Singleton02();
    //     }
    //     return INSTANCE;
    // }

    // 处理线程不安全问题
    private static volatile Singleton02 INSTANCE;
    public static Singleton02 getInstance() {
        if (INSTANCE == null) {
            synchronized(Singleton02.class){
                if(INSTANCE == null) INSTANCE = new Singleton02();
            }
        }
        return INSTANCE;
    }

}

/**
 * 静态内部类
 * JVM保证单例
 * 加载外部类时不会加载内部类，这样可以实现懒加载
 */
class Singleton03{
    private Singleton03(){}
    private static class Singleton03Holder{
        private final static Singleton03 INSTANCE = new Singleton03();
    }

    public static Singleton03 getInstance(){
        return Singleton03Holder.INSTANCE;
    }

}