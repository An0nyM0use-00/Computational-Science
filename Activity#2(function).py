def find_root(f, a, b, max_iter=100):
    if f(a) * f(b) > 0:
        print("Error: f(a) and f(b) must have opposite signs!")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2  
        
        if f(c) == 0:
            return c
            
        if f(a) * f(c) < 0:
            b = c 
        else:
            a = c 
    
    return (a + b) / 2

if __name__ == "__main__":
    func_str = input("Enter a continuous function f(x) (e.g., 'x**2 - 4' or 'x**3 + x - 1'): ")
    f = lambda x: eval(func_str) 
    
    a = float(input("Enter a (start of interval): "))
    b = float(input("Enter b (end of interval): "))
    
    root = find_root(f, a, b)
    
    if root is not None:
        print(f"\nApproximate root: x ≈ {root}")
        print(f"f(x) at root: {f(root)}")
