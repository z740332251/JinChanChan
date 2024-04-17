<template>
    <div>
        <!-- 用来显示GoJS图表的DIV -->
        <div id="myDiagramDiv" style="width: 100%; height: 600px;"></div>
    </div>
</template>

<script>
import go from 'gojs';

export default {
    data() {
        return {
            myDiagram: null,
        };
    },
    mounted() {
        // 在组件挂载后初始化GoJS图表
        this.init();
    },
    methods: {
        init() {
            const $ = go.GraphObject.make;
            // 初始化图表
            const myDiagram = $(go.Diagram, "myDiagramDiv", {
                "undoManager.isEnabled": true, // 启用撤销管理器
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
                    $(go.Shape, { strokeWidth: 2 }),  // 定义连接线形状
                    $(go.Shape, { toArrow: "Standard" })  // 定义箭头
                );
            // 设置节点数据
            myDiagram.model = new go.GraphLinksModel(
                [
                    { key: "Alpha", name: "Alpha", color: "lightblue" },
                    { key: "Beta", name: "Beta", color: "lightgreen" }
                ],
                [
                    { from: "Alpha", to: "Beta" }
                ]
            );
            // 将图表实例存储在组件的data中
            this.myDiagram = myDiagram;
        }
    }
};
</script>