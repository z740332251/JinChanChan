<template>
    <div>
        <!-- 用来显示GoJS图表的DIV -->
        <div id="myDiagramDiv" style="width: 100%; height: 1000px;"></div>
    </div>
</template>

<script>
///* eslint-disable */
import go from 'gojs';

export default {
    data() {
        return {
            myDiagram: null,
            heroNode: [],
            heroEdge: [],
            clickedLink: null // 存储当前点击的链接
        };
    },
    mounted() {
        this.initData();

        // 在组件挂载后初始化GoJS图表
        this.init();
    },
    methods: {
        initData() {
            let heroNode = [{ 'key': '1205', 'name': '盖伦', 'color': 'lightgreen' }, { 'key': '1206', 'name': '贾克斯', 'color': 'lightgreen' }, { 'key': '1207', 'name': '墨菲特', 'color': 'lightgreen' }, { 'key': '1208', 'name': '科加斯', 'color': 'lightgreen' }, { 'key': '1209', 'name': '卡兹克', 'color': 'lightgreen' }, { 'key': '1210', 'name': '德莱厄斯', 'color': 'lightgreen' }, { 'key': '1211', 'name': '雷克塞', 'color': 'lightgreen' }, { 'key': '1212', 'name': '亚索', 'color': 'lightgreen' }, { 'key': '1213', 'name': '希维尔', 'color': 'lightgreen' }, { 'key': '1214', 'name': '阿狸', 'color': 'lightgreen' }, { 'key': '1215', 'name': '凯特琳', 'color': 'lightgreen' }, { 'key': '1216', 'name': '可酷伯', 'color': 'lightgreen' }, { 'key': '1217', 'name': '克格莫', 'color': 'lightgreen' }, { 'key': '2195', 'name': '纳尔', 'color': 'lightgreen' }, { 'key': '2196', 'name': '亚托克斯', 'color': 'lightgreen' }, { 'key': '2197', 'name': '婕拉', 'color': 'lightgreen' }, { 'key': '2198', 'name': '拉克丝', 'color': 'lightgreen' }, { 'key': '2199', 'name': '慎', 'color': 'lightgreen' }, { 'key': '2302', 'name': '奇亚娜', 'color': 'lightgreen' }, { 'key': '2303', 'name': '妮蔻', 'color': 'lightgreen' }, { 'key': '2305', 'name': '千珏', 'color': 'lightgreen' }, { 'key': '2306', 'name': '锐雯', 'color': 'lightgreen' }, { 'key': '2307', 'name': '赛娜', 'color': 'lightgreen' }, { 'key': '2308', 'name': '约里克', 'color': 'lightgreen' }, { 'key': '2309', 'name': '迦娜', 'color': 'lightgreen' }, { 'key': '2310', 'name': '提莫', 'color': 'lightgreen' }, { 'key': '3211', 'name': '永恩', 'color': 'lightgreen' }, { 'key': '3212', 'name': '厄斐琉斯', 'color': 'lightgreen' }, { 'key': '3213', 'name': '巴德', 'color': 'lightgreen' }, { 'key': '3214', 'name': '拉露恩', 'color': 'lightgreen' }, { 'key': '3215', 'name': '阿木木', 'color': 'lightgreen' }, { 'key': '3216', 'name': '黛安娜', 'color': 'lightgreen' }, { 'key': '3217', 'name': '俄洛伊', 'color': 'lightgreen' }, { 'key': '3218', 'name': '佐伊', 'color': 'lightgreen' }, { 'key': '3219', 'name': '塔姆', 'color': 'lightgreen' }, { 'key': '3220', 'name': '崔丝塔娜', 'color': 'lightgreen' }, { 'key': '3221', 'name': '沃利贝尔', 'color': 'lightgreen' }, { 'key': '3222', 'name': '锤石', 'color': 'lightgreen' }, { 'key': '3223', 'name': '索拉卡', 'color': 'lightgreen' }, { 'key': '4201', 'name': '加里奥', 'color': 'lightgreen' }, { 'key': '4202', 'name': '莫甘娜', 'color': 'lightgreen' }, { 'key': '4203', 'name': '安妮', 'color': 'lightgreen' }, { 'key': '4205', 'name': '奥恩', 'color': 'lightgreen' }, { 'key': '4206', 'name': '莉莉娅', 'color': 'lightgreen' }, { 'key': '4207', 'name': '辛德拉', 'color': 'lightgreen' }, { 'key': '4209', 'name': '卡莎', 'color': 'lightgreen' }, { 'key': '4210', 'name': '凯隐', 'color': 'lightgreen' }, { 'key': '4212', 'name': '诺提勒斯', 'color': 'lightgreen' }, { 'key': '4213', 'name': '艾希', 'color': 'lightgreen' }, { 'key': '4214', 'name': '李青', 'color': 'lightgreen' }, { 'key': '4215', 'name': '塞拉斯', 'color': 'lightgreen' }, { 'key': '5175', 'name': '丽桑卓', 'color': 'lightgreen' }, { 'key': '5176', 'name': '瑟提', 'color': 'lightgreen' }, { 'key': '5177', 'name': '霞与洛', 'color': 'lightgreen' }, { 'key': '5178', 'name': '霞', 'color': 'lightgreen' }, { 'key': '5179', 'name': '洛', 'color': 'lightgreen' }, { 'key': '5180', 'name': '乌迪尔', 'color': 'lightgreen' }, { 'key': '5182', 'name': '彗', 'color': 'lightgreen' }, { 'key': '5183', 'name': '阿兹尔', 'color': 'lightgreen' }, { 'key': '5184', 'name': '艾瑞莉娅', 'color': 'lightgreen' }, { 'key': '5185', 'name': '孙悟空', 'color': 'lightgreen' }];
            let heroEdge = [{ 'from': '1205', 'to': '1206', 'text': '护卫' }, { 'from': '1206', 'to': '2195', 'text': '护卫' }, { 'from': '2195', 'to': '3215', 'text': '护卫' }, { 'from': '3215', 'to': '3217', 'text': '护卫' }, { 'from': '3217', 'to': '4212', 'text': '护卫' }, { 'from': '4212', 'to': '5176', 'text': '护卫' }, { 'from': '1205', 'to': '1213', 'text': '剪纸仙灵' }, { 'from': '1213', 'to': '2197', 'text': '剪纸仙灵' }, { 'from': '2197', 'to': '2306', 'text': '剪纸仙灵' }, { 'from': '2306', 'to': '3218', 'text': '剪纸仙灵' }, { 'from': '3218', 'to': '4201', 'text': '剪纸仙灵' }, { 'from': '4201', 'to': '5184', 'text': '剪纸仙灵' }, { 'from': '1206', 'to': '2196', 'text': '墨之影' }, { 'from': '2196', 'to': '2307', 'text': '墨之影' }, { 'from': '2307', 'to': '3221', 'text': '墨之影' }, { 'from': '3221', 'to': '4209', 'text': '墨之影' }, { 'from': '4209', 'to': '5180', 'text': '墨之影' }, { 'from': '1207', 'to': '1208', 'text': '擎天卫' }, { 'from': '1208', 'to': '2199', 'text': '擎天卫' }, { 'from': '2199', 'to': '2308', 'text': '擎天卫' }, { 'from': '2308', 'to': '3222', 'text': '擎天卫' }, { 'from': '3222', 'to': '4205', 'text': '擎天卫' }, { 'from': '4205', 'to': '5180', 'text': '擎天卫' }, { 'from': '1207', 'to': '1209', 'text': '天将' }, { 'from': '1209', 'to': '2302', 'text': '天将' }, { 'from': '2302', 'to': '2303', 'text': '天将' }, { 'from': '2303', 'to': '3223', 'text': '天将' }, { 'from': '3223', 'to': '5185', 'text': '天将' }, { 'from': '1208', 'to': '1217', 'text': '山海绘卷' }, { 'from': '1217', 'to': '2303', 'text': '山海绘卷' }, { 'from': '2303', 'to': '3213', 'text': '山海绘卷' }, { 'from': '3213', 'to': '3219', 'text': '山海绘卷' }, { 'from': '3219', 'to': '4206', 'text': '山海绘卷' }, { 'from': '4206', 'to': '4212', 'text': '山海绘卷' }, { 'from': '4212', 'to': '5182', 'text': '山海绘卷' }, { 'from': '1209', 'to': '2305', 'text': '死神' }, { 'from': '2305', 'to': '3211', 'text': '死神' }, { 'from': '3211', 'to': '4210', 'text': '死神' }, { 'from': '1210', 'to': '1212', 'text': '决斗大师' }, { 'from': '1212', 'to': '2302', 'text': '决斗大师' }, { 'from': '2302', 'to': '3220', 'text': '决斗大师' }, { 'from': '3220', 'to': '3221', 'text': '决斗大师' }, { 'from': '3221', 'to': '4214', 'text': '决斗大师' }, { 'from': '4214', 'to': '5184', 'text': '决斗大师' }, { 'from': '1210', 'to': '2308', 'text': '夜幽' }, { 'from': '2308', 'to': '3211', 'text': '夜幽' }, { 'from': '3211', 'to': '3214', 'text': '夜幽' }, { 'from': '3214', 'to': '4215', 'text': '夜幽' }, { 'from': '4215', 'to': '5176', 'text': '夜幽' }, { 'from': '1211', 'to': '1216', 'text': '斗士' }, { 'from': '1216', 'to': '2196', 'text': '斗士' }, { 'from': '2196', 'to': '2306', 'text': '斗士' }, { 'from': '2306', 'to': '3219', 'text': '斗士' }, { 'from': '3219', 'to': '4201', 'text': '斗士' }, { 'from': '4201', 'to': '4215', 'text': '斗士' }, { 'from': '1211', 'to': '2195', 'text': '永恒之森' }, { 'from': '2195', 'to': '2305', 'text': '永恒之森' }, { 'from': '2305', 'to': '4205', 'text': '永恒之森' }, { 'from': '4205', 'to': '5183', 'text': '永恒之森' }, { 'from': '1212', 'to': '1214', 'text': '灵魂莲华' }, { 'from': '1214', 'to': '2305', 'text': '灵魂莲华' }, { 'from': '2305', 'to': '3212', 'text': '灵魂莲华' }, { 'from': '3212', 'to': '3222', 'text': '灵魂莲华' }, { 'from': '3222', 'to': '4207', 'text': '灵魂莲华' }, { 'from': '4207', 'to': '5176', 'text': '灵魂莲华' }, { 'from': '1213', 'to': '2310', 'text': '迅捷射手' }, { 'from': '2310', 'to': '3213', 'text': '迅捷射手' }, { 'from': '3213', 'to': '4209', 'text': '迅捷射手' }, { 'from': '4209', 'to': '5177', 'text': '迅捷射手' }, { 'from': '5177', 'to': '5178', 'text': '迅捷射手' }, { 'from': '1214', 'to': '2198', 'text': '法师' }, { 'from': '2198', 'to': '2303', 'text': '法师' }, { 'from': '2303', 'to': '3217', 'text': '法师' }, { 'from': '3217', 'to': '3218', 'text': '法师' }, { 'from': '3218', 'to': '4207', 'text': '法师' }, { 'from': '4207', 'to': '5175', 'text': '法师' }, { 'from': '1215', 'to': '1217', 'text': '狙神' }, { 'from': '1217', 'to': '2307', 'text': '狙神' }, { 'from': '2307', 'to': '3212', 'text': '狙神' }, { 'from': '3212', 'to': '4213', 'text': '狙神' }, { 'from': '1215', 'to': '2196', 'text': '幽魂' }, { 'from': '2196', 'to': '2199', 'text': '幽魂' }, { 'from': '2199', 'to': '3217', 'text': '幽魂' }, { 'from': '3217', 'to': '4202', 'text': '幽魂' }, { 'from': '4202', 'to': '4210', 'text': '幽魂' }, { 'from': '1216', 'to': '2310', 'text': '吉星' }, { 'from': '2310', 'to': '3218', 'text': '吉星' }, { 'from': '3218', 'to': '3220', 'text': '吉星' }, { 'from': '3220', 'to': '4203', 'text': '吉星' }, { 'from': '1217', 'to': '2309', 'text': '神谕者' }, { 'from': '2309', 'to': '3214', 'text': '神谕者' }, { 'from': '3214', 'to': '4203', 'text': '神谕者' }, { 'from': '4203', 'to': '4206', 'text': '神谕者' }, { 'from': '4206', 'to': '5183', 'text': '神谕者' }, { 'from': '2197', 'to': '3216', 'text': '圣贤' }, { 'from': '3216', 'to': '4202', 'text': '圣贤' }, { 'from': '4202', 'to': '5185', 'text': '圣贤' }, { 'from': '2198', 'to': '3215', 'text': '青花瓷' }, { 'from': '3215', 'to': '4213', 'text': '青花瓷' }, { 'from': '4213', 'to': '5175', 'text': '青花瓷' }, { 'from': '2306', 'to': '3223', 'text': ' 武仙子' }, { 'from': '3223', 'to': '5177', 'text': '武仙子' }, { 'from': '5177', 'to': '5179', 'text': '武仙子' }, { 'from': '2309', 'to': '3216', 'text': '天龙之子' }, { 'from': '3216', 'to': '4214', 'text': '天龙之 子' }, { 'from': '4214', 'to': '5177', 'text': '天龙之子' }, { 'from': '5177', 'to': '5178', 'text': '天龙之子' }, { 'from': '5178', 'to': '5179', 'text': '天龙之子' }, { 'from': '5177', 'to': '5178', 'text': '仙侣' }, { 'from': '5178', 'to': '5179', 'text': '仙侣' }];
            this.heroNode = heroNode
            this.heroEdge = heroEdge
        },

        init() {
            const $ = go.GraphObject.make;
            // 初始化图表
            const myDiagram = $(go.Diagram, "myDiagramDiv", {
                "undoManager.isEnabled": true, // 启用撤销管理器
                "layout": $(go.TreeLayout), // 使用力导向布局 TreeLayout树形还行  LayeredDigraphLayout, { isInitial: true }) 
            });
            // 定义节点模板
            myDiagram.nodeTemplate =
                $(go.Node, "Auto",
                    $(go.Shape, "RoundedRectangle",  // 定义节点形状
                        { fill: "white" },  // 节点填充颜色
                        new go.Binding("fill", "color")),  // 绑定节点填充颜色
                    $(go.TextBlock,  // 定义节点文字
                        { margin: 8, editable: true },  // 文字边距和是否可编辑
                        new go.Binding("text", "name").makeTwoWay())  // 绑定节点文字内容
                );
            // 定义连接线模板
            myDiagram.linkTemplate =
                $(go.Link,
                    $(go.Shape, { strokeWidth: 1, stroke: "red", fill: "red" }),  // 定义连接线形状,
                    $(go.Shape, { toArrow: "Standard", stroke: "red", fill: "red" })  // 定义箭头
                );
            // 设置节点数据
            myDiagram.model = new go.GraphLinksModel(
                this.heroNode,
                this.heroEdge
            );

            // 为链接添加点击事件处理程序
            // myDiagram.addDiagramListener('ObjectSingleClicked', e => {
            //     const part = e.subject.part;
            //     if (part instanceof go.Link) {
            //         this.clickedLink = part;
            //         this.updateLinkOpacity();
            //     }
            // });

            // 将图表实例存储在组件的data中
            this.myDiagram = myDiagram;
        },
        updateLinkOpacity() {
            this.myDiagram.links.each(link => {
                if (link === this.clickedLink) {
                    link.elements.each(element => {
                        console.log(element)
                    });
                    link.findObject('text').opacity = 1; // 设置当前点击的链接文本不透明
                } else {
                    link.elements.each(element => {
                        console.log(element)
                    });
                    link.findObject('text').opacity = 0.5; // 设置其他链接文本半透明
                }
            });
        }
    }
};
</script>