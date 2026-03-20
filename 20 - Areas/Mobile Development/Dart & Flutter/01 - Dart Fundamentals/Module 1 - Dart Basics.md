# Study Note: Module 1 - Dart Basics
Subject: #study/dart 
Status: #study/learning 

## 📖 Key Concepts & Definitions
- **The Dart Virtual Machine (VM)**: Powers the runtime environment during development (Hot Reload).
- **AOT (Ahead-of-Time) Compilation**: Compiles code into fast machine code for production.
- **`main()` function**: Every Dart app starts execution here.
- **Variables**: `var`, `final`, `const`.
  - `final`: Set once, initialized at runtime.
  - `const`: Set once, initialized at compile-time (more efficient).

## 📝 Detailed Notes

### Basic Syntax & Types
```dart
void main() {
  // Types
  int age = 25;
  double price = 19.99;
  String name = 'Flutter Pro';
  bool isActive = true;

  // Type Inference
  var description = 'Bootcamp student'; // Type is String
  
  // Interpolation
  print('Hello $name, age is $age');
}
```

### Functions: The Dart Way
```dart
// Arrow Function
int add(int a, int b) => a + b;

// Named Parameters (Key for Flutter)
void greet({required String name, int? age}) {
  print('Hi $name ${age ?? ""}');
}
```

### Control Flow & Collections
- **Lists**: `List<String> fruits = ['Apple', 'Banana'];`
- **Maps**: `Map<String, dynamic> user = {'id': 1, 'name': 'Nick'};`
- **Conditionals**: Standard `if/else`, but Dart also has the **Null-aware Operator** (`??`) and **Null-conditional Operator** (`?.`).

## 🧠 Questions & Flashcards
- **Q**: What is the difference between `final` and `const`?
  - **A**: `final` is initialized when accessed at runtime; `const` is fixed at compile-time.
- **Q**: What does `void` mean in `void main()`?
  - **A**: It indicates that the function returns no value.

## ✍️ Practice / Application (Milestone 1)
- [ ] Install [Flutter SDK](https://docs.flutter.dev/get-started/install).
- [ ] Run `flutter doctor` and resolve all issues.
- [ ] Create a "Hello World" Dart script and run it in the terminal (`dart run hello.dart`).

## 📅 Review Schedule
- [ ] First Review (Today)
- [ ] Second Review (Tomorrow)
- [ ] Final Review (Next Week)
