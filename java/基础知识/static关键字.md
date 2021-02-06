## static 关键字

- **静态(static)**的变量和方法，在类加载时就会分配内存，可以直接通过类名调用
- **非静态**成员（变量和方法）属于类的对象，所以只有在类的对象产生（创建类的实例）时才会分配内存，然后通过类的对象（实例）去访问

### 如何定义

- 在定义的方法或属性之前加上**static**关键字

  ```java
  Class StaticTest{
  	static int i = 47;
  	public static void staticMethod(){}
  }
  ```

### 调用

- 不用创建对象，类名点直接调用

  ```java
  StaticTest.i;
  StaticTest.staticMethod();
  ```

- 静态(**static**)不能直接访问非静态，非静态能访问静态。(后人知道前人，而前人不知道后人（我认识秦始皇，但他不认识我）)

- 使用**new关键字**创建的对象调用，在编译时也是直接**类名.静态方法或属性**调用

  ```java
  StaticTest staticTest = new StaticTest();
  staticTest.staticMethod();
  ```

- 静态方法中不能使用**this**关键字

### 分配

- 多个对象共用内存

  ```java
  StaticTest staticTest1 = new StaticTest();
  StaticTest staticTest2 = new StaticTest();
  ```

- 创建了两个对象，**StaticTest.i**  只占用一份存储空间，两个对象共用**i**和**staticMethod**方法。

### 使用

- 定义一个学生的类
  - 其中教室是多个学生共用的，可以用**static**关键字。
  - 而学号是每个学生自己的，不用***static***关键字

  ```java
  class Student{
  	public String id;   // 学号
  	public static String classroom;    // 教室
      
      public static void main(String[] args){
          Student.classroom = "101";
          Student student1 = new Student();
          
      }
  }
  ```
  
  

### 静态代码块

- 在类加载的时候调用 

  ```java
  class Student{
  	static {
  		System.out.println("静态代码块");
  	}
  }
  ```

  



