
def list_slicing_demo():
    
    numbers = list(range(1, 11))
    print(f"Original list: {numbers}")
    
  
    first_five = numbers[:5]
    print(f"Extracted first five elements: {first_five}")
    
    
    reversed_five = first_five[::-1]
    print(f"Reversed extracted elements: {reversed_five}")


if __name__ == "__main__":
    list_slicing_demo()
