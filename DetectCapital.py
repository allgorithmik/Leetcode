def detectCapital(st: str) -> bool:
    if st.isupper():
        return True
    elif st.islower():
        return True
    elif st[0].isupper():
        return True
    else:
        return False

detectCapital() # Pass a string