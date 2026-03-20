# Study Note: RE Module 1 - Architecture & Binary Fundamentals
Subject: #study/reverse-engineering 
Status: #study/learning 

## 📖 Key Concepts & Definitions
- **The CPU**: The heart of RE. In x86_64, you must master the registers.
- **Endianness**: How bytes are ordered in memory. 
	- **Little-Endian (x86)**: Least significant byte at the lowest address (e.g., `0xAABBCCDD` becomes `DD CC BB AA`).
	- **Big-Endian (Network, ARM)**: Most significant byte first.
- **Two's Complement**: How the CPU represents negative numbers in binary.
- **The Stack**: A LIFO (Last-In, First-Out) data structure used for function calls, local variables, and return addresses.

## 📝 Detailed Notes

### x86_64 Register Map (The Essentials)
- **RAX**: Accumulator (Often used for function return values).
- **RBX**: Base register.
- **RCX**: Counter (Used in loops).
- **RDX**: Data register.
- **RSI / RDI**: Source and Destination indices (Used in string operations).
- **RSP**: Stack Pointer (Points to the *top* of the stack).
- **RBP**: Base Pointer (Points to the *base* of the current stack frame).
- **RIP**: Instruction Pointer (Points to the *next* instruction to execute).

### Memory Layout of a Process
1. **Stack**: Grows *downward* (toward lower memory addresses).
2. **Heap**: Grows *upward* (used for dynamic memory allocation: `malloc`).
3. **Data Segment**: Global/Static variables.
4. **Text (Code) Segment**: Read-only, where the instructions live.

## 🧠 Questions & Flashcards
- **Q**: If a function returns an integer in x86_64, which register will hold that value?
  - **A**: `RAX`.
- **Q**: What happens to `RSP` when a `PUSH` instruction is executed?
  - **A**: It is *decremented* (usually by 8 bytes in 64-bit) because the stack grows downward.

## ✍️ Practice / Application
- [ ] Install [Ghidra](https://ghidra-sre.org/) and [x64dbg](https://x64dbg.com/).
- [ ] Download a simple "Hello World" binary and identify its `main()` function in Ghidra.
- [ ] Use a hex editor to change a string in a binary and run it to see the change.

## 📅 Review Schedule
- [ ] First Review (Today)
- [ ] Second Review (Tomorrow)
- [ ] Final Review (Next Week)
