# Study Note: Module 1 - Kotlin Basics
Subject: #study/kotlin 
Status: #study/learning 

## 📖 Key Concepts & Definitions
- **The Kotlin Multiplatform (KMP)**: Kotlin is not just for Android; it can run on iOS, Web, and Desktop.
- **Null Safety**: Kotlin's type system is designed to eliminate `NullPointerException` through nullable types.
- **Interop**: Kotlin is 100% interoperable with Java.
- **Variables**: `val` vs `var`.
  - `val`: Immutable reference (Read-only, like `final` in Java).
  - `var`: Mutable reference (Can be reassigned).

## 📝 Detailed Notes

### Basic Syntax & Types
```kotlin
fun main() {
    // Variables
    val name = "Nick" // Type inferred as String
    var score: Int = 0 // Explicit type

    // String Templates
    println("Welcome, $name! Your score is $score.")

    // Nullable types
    var nullableName: String? = null
    println(nullableName?.length ?: "No name provided")
}
```

### Functions & Lambdas
```kotlin
// Single-expression function
fun multiply(a: Int, b: Int) = a * b

// Function with default arguments
fun greet(name: String = "Guest") {
    println("Hello, $name!")
}

// Lambda expression
val sum: (Int, Int) -> Int = { x, y -> x + y }
```

### Control Flow: The Power of `When`
```kotlin
val result = when (score) {
    in 1..50 -> "Keep practicing"
    in 51..90 -> "Great job"
    else -> "Mastered"
}
```

## 🧠 Questions & Flashcards
- **Q**: What is the difference between `val` and `var`?
  - **A**: `val` is immutable; `var` is mutable.
- **Q**: What does the `?.` operator do in Kotlin?
  - **A**: It is the "Safe Call" operator. It only executes the following property/method if the object is not null.

## ✍️ Practice / Application
- [ ] Install [Android Studio (Ladybug or latest)](https://developer.android.com/studio).
- [ ] Create a new project using the **Empty Compose Activity** template.
- [ ] Experiment with Kotlin syntax in the **Kotlin Playground** (online) or a scratch file in Android Studio.

## 📅 Review Schedule
- [ ] First Review (Today)
- [ ] Second Review (Tomorrow)
- [ ] Final Review (Next Week)
