#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
goodies = dir(hidden_4)
for goods in goodies:
    if goods[:2] != "__":
        print(goods)
