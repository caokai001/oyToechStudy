## 1.R 循环
[参考](https://www.jianshu.com/p/ad98c92c2da1)
```
pf<-function(x){
  if (x>5){
    return(x*x)}
  else{
    return(2*x)
  }
}
pf(4)
###*pply函数
sapply(1:6,pf)
lapply(1:6,pf)
### 向量
A=c()
for (i in 1:6){
  A=cbind(A,pf(i))
}
print(A)
### 空matrix
A=matrix(NA,1,6,byrow = F)
for (i in 1:6){
  A[1,i]=pf(i)
}
print(A)

```
