import time
from report import CuboReport
from scraping import ScrapScrap

class CuboSearch:

    def __init__(self, chrome_path, url, element):
        self.bot = ScrapScrap(chrome_path=chrome_path)
        self.bot.get(url)
        self.bot.refresh()
        self.bot.refresh()
        self.bot.wait(element)

        self.report = CuboReport()
        self.report.create_df_startup()

        # for i in range(0, 50):
        #     self.bot.scroll_down()
        #     time.sleep(1)

        # self.bot.maximize()
        
    def loop(self):
        startups = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-list/section/div[4]/div/*[@class='startups__item ng-star-inserted']", "find")
        for startup in startups:
            self.report.insert_startup(link_cubo=startup.get_attribute('href'))

        for index, row in self.report.df_startup.iterrows():
            self.bot.get(row['Link cubo'])

            time.sleep(10)

            try:
                name = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-header-company/p", "text")
            except Exception as e:
                print(e)
                name = None
            try:
                first = self.bot.find_all_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[1]/article/*", "find")
                core = ""
                area = ""
                vertical = ""
                for i in first:
                    if i.find_element_by_xpath(".//h1[@class='title']").text == "Area":
                        _area = i.find_elements_by_xpath(".//cb-chip-list/*")
                        for j in _area:
                            area = j.find_element_by_xpath(".//div").text + " + " + area
                    elif i.find_element_by_xpath(".//h1[@class='title']").text == "Core Business":
                        _core = i.find_elements_by_xpath(".//cb-chip-list/*")
                        for j in _core:
                            core =  j.find_element_by_xpath(".//div").text + " + " + core
                    elif i.find_element_by_xpath(".//h1[@class='title']").text == "Vertical":
                        _vertical = i.find_elements_by_xpath(".//cb-chip-list/*")
                        for j in _vertical:
                            vertical = j.find_element_by_xpath(".//div").text + " + " + vertical

                row["Nome"] = str(name)
                row["Core business"] = str(core)
                row["Vertical"] = str(vertical)
                row["Area"] = str(area)

            except Exception as e:
                print(e)
                pass

            try:
                # second = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[2]/article/cb-accordion/header/span[1]", "text")
                # row[str(second)] = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[2]/article/cb-accordion/section/app-translator/div[2]", "text")
                problem = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[2]/article/cb-accordion/section/app-translator/div[2]", "text")
            except Exception as e:
                problem = None
                print("SECOND")
                print(e)

            try:
                # third = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[3]/article/cb-accordion/header/span[1]", "text")
                # row[str(third)] = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[3]/article/cb-accordion/section/app-translator/div[2]", "text")
                pitch = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[3]/article/cb-accordion/section/app-translator/div[2]", "text")
            except Exception as e:
                pitch = None
                print("THIRD")
                print(e)

            try:
                # four = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[4]/article/cb-accordion/header/span[1]", "text")
                # row[str(four)] = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[4]/article/cb-accordion/section/app-translator/div[2]", "text")
                diff = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[4]/article/cb-accordion/section/app-translator/div[2]", "text")
            except Exception as e:
                diff = None
                print("FOUR")
                print(e)
                pass

            try:
                business = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[5]/article/cb-chip-list/cb-chip/div", "text")
            except:
                business = None
            try:
                website = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[9]/article/a", "text")
            except:
                website = None
            try:
                address = self.bot.find_xpath("/html/body/app-cubo/main/page-startups-detail/section/div/app-section-profile[10]/article/address/span", "text")
            except:
                address = None


            row["What problem do we solve"] = str(problem)
            row["Pitch"] = str(pitch)
            row["Market Differentials"] = str(diff)
            # row["Bussiness Model"] = str(business)
            # row["Website"] = str(website)
            # row["Address"] = str(address)
            # print(self.report.df_startup)

        self.report.df_startup.to_csv("startup.csv", index = False)

chrome_path = r"/home/felipe/Documents/chromedriver"
url = "https://cubo.network/startups"
element = "/html/body/app-cubo/app-header/header/a/img"

cubo = CuboSearch(chrome_path=chrome_path, url=url, element=element)
cubo.loop()