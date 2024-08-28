row1='|_|_|_|'
row2='|_|_|_|'
row3='|_|_|_|'


def display_board():
    
    print('The current board is:')
    
    print(row1)
    print(row2)
    print(row3)
display_board()
a=list(row1)
b=list(row2)
c=list(row3)
def player1():
    
    print("Player 1 is assigned with 'X' value\n")
    
    
    
    row=''
    position=''
    
    while row.isdigit()==False or row not in [1,2,3]:
        
        
        
        row=input("Enter a row of choice between 1,2 and 3: ")
        
        
        if row.isdigit()==False:
            
             print("Hey! That's not a digit.")
        
        if row.isdigit()==True:
            
            if int(row) in [1,2,3]:
                
                
                while position.isdigit()==False or position not in [0,1,2]:
            
                   position=input("Enter the position of insertion between 0,1 and 2: ")
            
                   if position.isdigit()==False:
            
                         print("Hey! That's not a digit.")
        
                   if position.isdigit()==True:
            
                         if int(position) not in [0,1,2]:
                    
                
                            print('Please enter a value within range.')
            
                         else:
                
                            return row,position
            else:
                
                print('Please enter a value within range.')
value=player1()
def replacement1():
    
    x=int(value[0])
    
    y=int(value[1])
    
    if x==1:
        
        if y==0:
            
            a[1]='X'
        if y==1:
            
            a[3]='X'
            
        if y==2:
            
            a[5]='X'
            
    if x==2:
        
        if y==0:
            
            b[1]='X'
        if y==1:
            
            b[3]='X'
            
        if y==2:
            
            b[5]='X'
            
    if x==3:
        
        if y==0:
            
            c[1]='X'
        if y==1:
            
            c[3]='X'
            
        if y==2:
            
            c[5]='X'
replacement1()
d=''.join(a)
e=''.join(b)
f=''.join(c)

def new_display():
    
    print(d)
    print(e)
    print(f)
new_display()
def player2():
    
    
    
    row=''
    position=''
    
    print("Player 2 is assigned with 'O' value")
    
    while row.isdigit()==False or row not in [1,2,3]:
        
        
        
        row=input("Enter a row of choice between 1,2 and 3: ")
        
        
        if row.isdigit()==False:
            
             print("Hey! That's not a digit.")
        
        if row.isdigit()==True:
            
            if int(row) in [1,2,3]:
                
                
                while position.isdigit()==False or position not in [0,1,2]:
            
                   position=input("Enter the position of insertion between 0,1 and 2: ")
            
                   if position.isdigit()==False:
            
                         print("Hey! That's not a digit.")
        
                   if position.isdigit()==True:
            
                         if int(position) not in [0,1,2]:
                    
                
                            print('Please enter a value within range.')
            
                         else:
                
                            return row,position
                            
    
                
               
            
            else:
                
                print('Please enter a value within range.')
value=player2()
def replacement2():
    
    x=int(value[0])
    
    y=int(value[1])
    
    if x==1:
        
        if y==0:
            
            a[1]='O'
        if y==1:
            
            a[3]='O'
            
        if y==2:
            
            a[5]='O'
            
    if x==2:
        
        if y==0:
            
            b[1]='O'
        if y==1:
            
            b[3]='O'
            
        if y==2:
            
            b[5]='O'
            
    if x==3:
        
        if y==0:
            
            c[1]='O'
        if y==1:
            
            c[3]='O'
            
        if y==2:
            
            c[5]='O'
replacement2()
d=''.join(a)
e=''.join(b)
f=''.join(c)

def new_display():
    
    print(d)
    print(e)
    print(f)
new_display()
def condition_check():
    if d[1]=='X':
        if d[3]==d[5]=='X':
            return ('Player 1 wins!')
        if e[1]==f[1]=='X':
            return ('Player 1 wins!')
        if e[3]==f[5]=='X':
            return ('Player 1 wins!')
    if d[3]=='X':
        if e[3]==f[3]=='X':
            return ('Player 1 wins!')
    if d[5]=='X':
        if e[5]==f[5]=='X':
            return ('Player 1 wins!')
        if e[3]==f[1]=='X':
            return ('Player 1 wins!')
    if e[1]==e[3]==e[5]=='X':
        return ('Player 1 wins!')
    if f[1]==f[3]==f[5]=='X':
        return ('Player 1 wins!')
        
        
    if d[1]=='O':
        if d[3]==d[5]=='O':
            return ('Player 2 wins!')
        if e[1]==f[1]=='O':
            return ('Player 2 wins!')
        if e[3]==f[5]=='O':
            return ('Player 2 wins!')
    if d[3]=='O':
        if e[3]==f[3]=='O':
            return ('Player 2 wins!')
    if d[5]=='O':
        if e[5]==f[5]=='O':
            return ('Player 2 wins!')
        if e[3]==f[1]=='O':
            return ('Player 2 wins!')
    if e[1]==e[3]==e[5]=='O':
        return ('Player 2 wins!')
    if f[1]==f[3]==f[5]=='O':
        return ('Player 2 wins!')
result=condition_check()
result
def gameon_choice():
    
    choice=''
    
    while choice not in ['yes','no']:
        
        choice=input('Do you want to continue?(yes or no): ')
            
        if choice not in ['yes','no']:
                
                print('The input is invalid!')
    
    if choice=='yes':
        
        return True
    else:
        
        return False
gameon_choice()
from IPython.display import clear_output
game_on=True

turn=''


row1='|_|_|_|'
row2='|_|_|_|'
row3='|_|_|_|'

while game_on==True:
    
    clear_output()
    display_board()
    
    a=list(row1)
    b=list(row2)
    c=list(row3)

    
    for turn in range(0,9):
        
        if turn%2==0:
            
            value=player1()
        
            replacement1()
            
        else:
            
            value=player2()
        
            replacement2()
            
        
           
        
        d=''.join(a)
        e=''.join(b)
        f=''.join(c)
            
        result=condition_check()
        
        new_display()
            
        if result=='Player 1 wins!' or result=='Player 2 wins!':
            
            print(result)
                
            game_on=gameon_choice()
            
            print(turn)
            
            break
            
   
    if turn>9:
        
        
   
        print("Oops the match is a tie!")
    
        game_on=gameon_choice()



    

