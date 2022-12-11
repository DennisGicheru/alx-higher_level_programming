#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    item = dir(hidden_4)

    for i in range(len(item)):
        for j in range(len(item[i])):
            if (item[i][j] == '_' and item[i][j+1] == '_'):
                break
            
            else:
                print(item[i])
                break    
