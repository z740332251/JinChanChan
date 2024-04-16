# 非原创，代码参见https://blog.csdn.net/qq_44407005/article/details/136842353
# 稍有改动，后期可能会进行更大的改动

# TODO 预期应该会将英雄作为顶点，羁绊作为边生成一个图，这个图并不要求点与点必须按照边相连，隔着其他同羁绊的边相连也可以
# 有向图，完全可以按照heroId作为有向图前后的依据，id越大星级越高·

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 设置Chrome驱动服务
service = Service(ChromeDriverManager().install())

# 创建Chrome浏览器实例
driver = webdriver.Chrome(service=service)

# 创建空的DataFrame来存储数据
data = {
    "英雄名称": [],
    "英雄技能": [],
    "技能描述": [],
    "属性信息": [],
    "羁绊信息": [],
    "费用":[]
}
print(pd.__version__)
# TODO 画之灵版本，每次版更需要重新捞数据
stars = [
    [1205, 1217 + 1],
    [2195, 2310 + 1],
    [3211, 3223 + 1],
    [4201, 4215 + 1],
    [5175, 5185 + 1]
]

df = pd.DataFrame(data)

# stars里面已经按照费用去排列好了，直接使用索引即可
priceNew = 0
# 循环遍历英雄ID范围
for star in stars:
    priceNew += 1
    for hero_id in range(star[0], star[1]):
        try:
            # 构建URL
            #url = f"https://jcc.qq.com/#/heroDetail/10,S11,10.4.5/{hero_id}"
            #画之灵版本
            url = f"https://jcc.qq.com/#/heroDetail/11,S12,12.4.7/{hero_id}"
            driver.get(url)

            # 获取页面内容
            html_content = driver.page_source

            # 使用Beautiful Soup解析HTML
            soup = BeautifulSoup(html_content, "html.parser")

            # 找到英雄详情的容器
            heroDetailWrap = soup.find("div", class_="hero-detail-wrap")
            if heroDetailWrap is None:
                continue

            # 提取英雄信息
            hero_name = heroDetailWrap.find("p", class_="name").text
            hero_skill = heroDetailWrap.find("p", class_="title skill-name").text.strip()
            hero_skill_description = heroDetailWrap.find("p", class_="active").text.strip()

            #TODO 费用
            price_element = heroDetailWrap.find("li", class_="price1")
            price = price_element.text.strip() if price_element else None

            # 提取属性信息
            attributes = heroDetailWrap.find("div", class_="attri").find_all("td")
            attributes_info = [attr.text for attr in attributes]

            # 提取羁绊信息
            synergy_names = heroDetailWrap.find_all("p", class_="title skill-name")

            # 构建一个字典以便将数据添加到DataFrame
            hero_data = {
                "英雄名称": hero_name,
                "英雄技能": hero_skill,
                "技能描述": hero_skill_description,
                "属性信息": "\n".join(attributes_info),
                "羁绊信息": ",".join([name.text for name in synergy_names[1:]]),  # 跳过第一个元素（英雄技能）
                "费用": priceNew
            }

            # 将字典转换为DataFrame并追加到现有DataFrame
            df = df._append(pd.DataFrame(hero_data, index=[0]), ignore_index=True)

        except Exception as e:
            print(e)
            print(f"Hero with ID {hero_id} does not exist.")

# 关闭浏览器
driver.quit()

# 保存DataFrame到Excel文件
df.to_excel("hero_details.xlsx", index=False)