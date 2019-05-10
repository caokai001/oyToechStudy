###记录

- 1.ggplot title居中 `+theme(plot.title = element_text(hjust = 0.5))`
```
df$pvalue%>%as.data.frame()%>%ggplot(aes(x=df$pvalue))+geom_histogram(binwidth = 0.01)+xlab("P-value")+ggtitle("41.result.csv")+theme_classic()+theme(plot.title = element_text(hjust = 0.5))
```
[图片](https://upload-images.jianshu.io/upload_images/9589088-9c2c5bd79a1e320b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/620/format/webp)

- 2.[dplyr大全](https://blog.csdn.net/wltom1985/article/details/54973811)
1.  数据集类型转换
2.   筛选:  filter
3. 排列: arrange
4. 选择: select
5.变形: mutate
6. 去重: distinct
7. 概括: summarise
8. 抽样: sample
9. 分组: group
10. 数据关联：join
11. 集合操作: set
12. 数据合并: bind
13. 条件语句：ifelse
14. 数据库操作: database