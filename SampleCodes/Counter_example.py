from collections import Counter


def main():
    no_of_shoes = int(input().strip())
    #print(no_of_shoes)
    shoe_list = input().strip().split()
    #print(Counter(shoe_list)['6'])
    shoe_dict = Counter(shoe_list)
    '''print(shoe_dict['6'])
    print(list(Counter(shoe_list).items()))
    print(list(Counter(shoe_list).keys()))
    print(list(Counter(shoe_list).values()))'''
    no_of_cust = int(input())
    total_price = 0
    for i in range(no_of_cust):
        size,price = input().strip().split()
        if ((size in list(shoe_dict.keys())) and (shoe_dict[size] != 0)):
            total_price = total_price + int(price)
            shoe_dict[size] = shoe_dict[size] - 1
    print(total_price)
            
    
if __name__ == '__main__':
    main()