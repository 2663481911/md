### kotlin中使用javaScript

```kotlin
import javax.script.ScriptEngine
import javax.script.ScriptEngineManager
```

#### 获取脚本引擎 

```kotlin
val scriptEngineManager = ScriptEngineManager()
val engine: ScriptEngine = scriptEngineManager.getEngineByName("javascript")
```

#### 绑定对象

```kotlin
engine.put("data", "data")
```

- 可以在脚本中使用

#### 执行脚本

```kotlin
engin.eval("println(data)")
```

- data 为上面绑定的**data**