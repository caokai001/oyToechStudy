###记录

- 1.ggplot title居中 `+theme(plot.title = element_text(hjust = 0.5))`
```
df$pvalue%>%as.data.frame()%>%ggplot(aes(x=df$pvalue))+geom_histogram(binwidth = 0.01)+xlab("P-value")+ggtitle("41.result.csv")+theme_classic()+theme(plot.title = element_text(hjust = 0.5))
```
[图片](https://upload-images.jianshu.io/upload_images/9589088-9c2c5bd79a1e320b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/620/format/webp)
