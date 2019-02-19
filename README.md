# A35Helper
一些用来管理索尼A35播放器音乐的工具
<br><br>

 - checksame.py
 
    用来检查两个文件夹里的文件是否有相同的项目
    - 使用方法：进入脚本后，输入需要检索的两个文件夹路径即可。稍后脚本将会输出一个`same.txt`，里面包含了输入两个文件夹下相同的文件的名称，每一行一个，可以配合`rm_list.py`删除重复文件
    - 注意事项：只能使用英文路径（以后的版本会完善）
    <br>
    
 - create_playlist.py
 
    取自于 [NeteaseCloudMusicPlaylistCreator](https://github.com/vileer/NeteaseCloudMusicPlaylistCreator)
    - 使用方法：直接运行，脚本便会检索本地网易云音乐缓存，并且在当前目录下输出`XXX.m3u`文件，"XXX"是网易云音乐中的歌单名
    - 注意事项：目前只能输出在某个时间点之前创建的歌单
    <br>
    
 - m3uMaker.py

    对当前文件夹下的所有mp3文件做成一个m3u播放列表
    - 使用方法：在有`*.mp3`的目录里直接运行，即可。会生成一个`1.m3u`歌单文件
    - 注意事项：目前只包含mp3文件，若有其他需求，可自行对源代码修改
    <br>
    
 - rm_list.py
 
    指定一个列表，根据列表删除相应的文件
    - 使用方法：运行后，输入列表文件所在路径（或将列表文件拖进控制台），脚本将会对列表中的文件进行删除
    <br>
    
 - lrc_rebuild.py
 
    若对歌曲使用 [ZonyLrcToolsX](https://github.com/GameBelial/ZonyLrcToolsX) 生成歌词文件，且歌曲同时也有翻译歌词时，原文和翻译的两个时间轴将会同时串在一起。虽然时间轴对歌词的映射并没有问题，但是某些时间在前的歌词却被错误地排到了后面
    <br>这个脚本的作用是，对已生成的歌词文件重写一遍，使时间轴重新排序
     
