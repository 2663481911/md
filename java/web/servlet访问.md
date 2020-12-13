## 浏览器访问Servlet.class文件方法

- 可以通过  `http://localhost:8080/servlet`  访问servlet文件
  - web.xml文件，添加以下内容

  ```xml
  <servlet>
      <servlet-name>MyServlet</servlet-name>
      <servlet-class>com.servlet.MyServlet</servlet-class>
  </servlet>
  
  <servlet-mapping>
      <servlet-name>MyServlet</servlet-name>
      <url-pattern>/servlet</url-pattern>
  </servlet-mapping>
  ```
  - 基于注解

  ```java
  @WebServlet("/servlet")
  public class MyServlet implements Servlet {...}
  ```


### 获取参数

- **getParameter()：**您可以调用 request.getParameter() 方法来获取表单参数的值。
- **getParameterValues()：**如果参数出现一次以上，则调用该方法，并返回多个值，例如复选框。
- **getParameterNames()：**如果您想要得到当前请求中的所有参数的完整列表，则调用该方法。

