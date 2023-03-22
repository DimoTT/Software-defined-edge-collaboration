with open('FLYOLOtrain_history2_loss.txt') as f:
  read_data=f.read()
  a=read_data.split(',')
  for i in range(0,1000):
    print(a[i])#这一行可以单独打印第几个字符串
f.closed