# Roadmap: Reverse Engineering Mastery
Subject: #study/cybersecurity #study/reverse-engineering #study/binary-exploitation 
Status: #status/active 

## 🛠️ Module-Based Learning Path (Specialized for Cyber Sec)

### Phase 1: Foundations (The Low-Level)
1. **01 - RE Fundamentals (CPU & Binary)**
	- [ ] CPU Architecture: Registers (GPRs, Segment, Control).
	- [ ] Memory Segments: Stack, Heap, Text, Data.
	- [ ] Binary Representation: Two's Complement, Endianness (Little vs. Big).
2. **02 - Assembly Mastery (x86_64)**
	- [ ] Instruction Set: Data movement (`MOV`, `PUSH`, `POP`), Arithmetic (`ADD`, `SUB`, `XOR`), Control Flow (`JMP`, `CALL`, `RET`).
	- [ ] Calling Conventions: `cdecl`, `stdcall`, `fastcall` (System V AMD64 ABI vs. MS x64).
	- [ ] Identifying High-Level Constructs: `if/else`, `for/while` loops, Switch-Case in Assembly.

### Phase 2: Static & Dynamic Analysis (The Core)
3. **03 - Static Analysis & Disassemblers**
	- [ ] Tools: **Ghidra** (The Go-To), **IDA Pro** (The Standard), **Binary Ninja**.
	- [ ] Code Graphing & Function Call Graphs.
	- [ ] Data-Flow Analysis: Understanding how values move through registers.
4. **04 - Dynamic Analysis & Debuggers**
	- [ ] Tools: **x64dbg** (Windows), **GDB** (Linux), **OllyDbg**.
	- [ ] Software vs. Hardware Breakpoints.
	- [ ] Patching Binaries: Modifying instructions (e.g., `JZ` to `JNZ`) to bypass checks.

### Phase 3: Binary Deep-Dive (OS Internals)
5. **05 - File Formats (PE, ELF, Mach-O)**
	- [ ] **Portable Executable (PE)**: Headers (DOS, File, Optional), Section Table, IAT/EAT.
	- [ ] **Executable and Linkable Format (ELF)**: Symbol tables, Dynamic linking.
6. **06 - Decompilation & Scripting**
	- [ ] Recovering C/C++ source code from assembly.
	- [ ] Scripting with **Ghidra Python** or **IDA Python** for automation.

### Phase 4: Advanced Cyber Sec Applications
7. **07 - Malware Reverse Engineering**
	- [ ] Unpacking Packed Malware (UPX, Custom packers).
	- [ ] Analysis of Malware Persistence Mechanisms.
	- [ ] Reverse engineering C2 (Command & Control) protocols.
8. **08 - Software Protection & Anti-RE**
	- [ ] Anti-Debugging Tricks: `IsDebuggerPresent`, Timing checks, Exception handling.
	- [ ] Obfuscation: Control Flow Flattening, Junk code, Virtualization-based protection (VMProtect).

## 📚 Essential Resources
- [Practical Reverse Engineering (Book)]
- [Reverse Engineering for Beginners (Dennis Yurichev)]
- [Crackmes.one (Practice Targets)]

## 📝 Active Study Notes
- [[20 - Areas/Cyber Security/Reverse Engineering/01 - RE Fundamentals (CPU & Binary)/RE Module 1 - Architecture & Binary Fundamentals|RE Module 1 - Architecture & Binary Fundamentals]]

- [[20 - Areas/Cyber Security/Reverse Engineering/02 - Assembly Mastery (x86_64)/Assembly Mastery (x86_64).md|Assembly Mastery (x86_64)]]
- [[20 - Areas/Cyber Security/Reverse Engineering/03 - Static Analysis & Disassemblers/Static Analysis & Disassemblers.md|Static Analysis & Disassemblers]]
- [[20 - Areas/Cyber Security/Reverse Engineering/04 - Dynamic Analysis & Debuggers/Dynamic Analysis & Debuggers.md|Dynamic Analysis & Debuggers]]
- [[20 - Areas/Cyber Security/Reverse Engineering/05 - File Formats (PE, ELF, Mach-O)/File Formats (PE, ELF, Mach-O).md|File Formats (PE, ELF, Mach-O)]]
- [[20 - Areas/Cyber Security/Reverse Engineering/06 - Decompilation & Scripting/Decompilation & Scripting.md|Decompilation & Scripting]]
- [[20 - Areas/Cyber Security/Reverse Engineering/07 - Malware Reverse Engineering/Malware Reverse Engineering.md|Malware Reverse Engineering]]
- [[20 - Areas/Cyber Security/Reverse Engineering/08 - Software Protection & Anti-RE/Software Protection & Anti-RE.md|Software Protection & Anti-RE]]