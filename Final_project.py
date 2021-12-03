import math
import numpy as np
import matplotlib.pyplot as plt
from Heat_map_gen import heatmapgen

f = open('SixCountries.txt','r')
f.readline()
data = f.readlines()

#generate arrays from inported files
Months = []
Dates = []

TotCases1 = []
TotCases2 = []
TotCases3 = []
TotCases4 = []
TotCases5 = []
TotCases6 = []

DNCases1 = []
DNCases2 = []
DNCases3 = []
DNCases4 = []
DNCases5 = []
DNCases6 = []

for line in data:
    Line = line.split()
    #print(Line)
    Months.append(Line[0])    
    Dates.append(Line[1])
    
    TotCases1.append(float(Line[3]))
    DNCases1.append(float(Line[4]))
    
    TotCases2.append(float(Line[6]))
    DNCases2.append(float(Line[7]))
    
    TotCases3.append(float(Line[9]))
    DNCases3.append(float(Line[10]))
    
    TotCases4.append(float(Line[12]))
    DNCases4.append(float(Line[13]))
    
    TotCases5.append(float(Line[15]))
    DNCases5.append(float(Line[16]))
    
    TotCases6.append(float(Line[18]))
    DNCases6.append(float(Line[19]))

f.close()


#user country selection
print('Country List\n------------\nNigeria\nChina\nRussia\nUSA\nBrazil\nAustralia')
#country selection
cs = input('Please select a country to observe: ')

#convert input to all lowercase 
cs = cs.lower()

#check for valid input
while cs != 'nigeria' and cs != 'china' and cs != 'russia' and cs != 'usa' and cs != 'brazil' and cs != 'australia':
    print('please enter a valid country name from list!')
    cs = input('Please select a country to observe: ')
print('Loading....')



#generate graph based off selected country
if cs == 'nigeria':
    print('Nigeria Regualation Timeline:\n\n')
    print('All regulations and mandates put into place in 2020.\n\n')
    print('On March 18, Nigeria bans travel to 13 countries.\n\n')
    print('On March 19, the federal government orders the closure of schools.\n\n')
    print('On March 23, international flights are banned and the government announces stimulus packages for households, SMEs, and the health sector.\n\n')
    print('On March 30, a lockdown is put into effect for many of it''s states.\n\n')
    print('On April 20, domestic flights are banned.\n\n')
    print('On May 2, Nationwide overnight curfews are put into effect.\n\n')
    print('On May 4, face masks are made mandatory when out in public.\n\n')
    print('https://www.brookings.edu/blog/future-development/2020/07/02/how-well-has-nigeria-responded-to-covid-19/')
    
    #Plot Total Number of Cases
    fig1, ax1 = plt.subplots()
    ax1.bar(Months,TotCases1)
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Number of Total Cases')
    ax1.set_title('Nigeria - Total Cases Over Time')
    fig1.set_size_inches(18.5, 10.5)
    
    #Plot Daily New Cases
    fig2, ax2 = plt.subplots()
    ax2.plot(Dates, DNCases1)
    ax2.set_xlabel('February 2020 - July 2021')
    ax2.set_ylabel('Number of Daily New Cases')
    ax2.set_title('Nigeria - Daily New Cases Over Time')
    fig2.set_size_inches(18.5, 10.5)
    plt.xticks(Dates,"")

    #generate heat map gif
    heatmapgen('Nigeria',TotCases1,206000000,310,140,20,200)
    
elif cs == 'china':
    print('China Regualtion Timeline:\n\n')
    print('All regulations and mandates put into place in 2020.\n\n')
    print('On January 23, major cities shit down public transit, trains, airports, and major highways.\n\n')
    print('On January 24, China enacts travel restrictions in major cities.\n\n')
    print('On February 20, China shuts down non-essential companies and factories.\n\n')
    print('On January 24, China enacts travel restrictions in major cities.\n\n')
    print('http://www.xinhuanet.com/2020-02/20/c_1125603476.htm\n\n')
    print('http://baijiahao.baidu.com/s?id=1658402162460563869')
    
    #Plot Total Number of Cases
    fig3, ax3 = plt.subplots()
    ax3.bar(Months, TotCases2)
    ax3.set_xlabel('Months')
    ax3.set_ylabel('Number of Total Cases')
    ax3.set_title('China - Total Cases Over Time')
    fig3.set_size_inches(18.5, 10.5)
    
    #Plot Daily New Cases
    fig4, ax4 = plt.subplots()
    ax4.plot(Dates, DNCases2)
    ax4.set_xlabel('February 2020 - July 2021')
    ax4.set_ylabel('Number of Daily New Cases')
    ax4.set_title('China - Daily New Cases Over Time')
    fig4.set_size_inches(18.5, 10.5)
    plt.xticks(Dates,"")

    #generate heat map gif
    heatmapgen('China',TotCases2,1402000000,750,350,20,200)
    
elif cs == 'russia':
    print('Russia Regulation Timeline:\n\n')
    print('All regulations and mandates put into place in 2020.\n\n')
    print('On January 31, Russia closes its Eastern border with China.\n\n')
    print('On March 16, Russia starts looking into vaccine prototypes.\n\n')
    print('On March 18, Russia starts banning entry to most foreign nationals.\n\n')
    print('On March 27, Russia stops all international air travel.\n\n')
    print('On April 13, Russia enacts lockdowns in major cities and populated areas.\n\n')
    print('On November 3, Russia puts a curfew on non-essential businesses.\n\n')
    print('https://www.themoscowtimes.com/2020/12/21/russias-response-to-the-coronavirus-the-2020-timeline-a72420')
    
    #Plot Total Number of Cases
    fig5, ax5 = plt.subplots()
    ax5.bar(Months, TotCases3)
    ax5.set_xlabel('Months')
    ax5.set_ylabel('Number of Total Cases')
    ax5.set_title('Russia - Total Cases Over Time')
    fig5.set_size_inches(18.5, 10.5)
    
    #Plot Daily New Cases
    fig6, ax6 = plt.subplots()
    ax6.plot(Dates, DNCases3)
    ax6.set_xlabel('February 2020 - July 2021')
    ax6.set_ylabel('Number of Daily New Cases')
    ax6.set_title('Russia - Daily New Cases Over Time')
    fig6.set_size_inches(18.5, 10.5)
    plt.xticks(Dates,"")

    #generate heat map gif
    heatmapgen('Russia',TotCases3,144000000,80,30,20,200)

    
elif cs == 'usa':
    print('USA Regulation Timeline:\n\n'
    'January 31 2020\n\nWHO Issues Global Health Emergency with a worldwide death toll of more than 200 and an exponential jump to more than 9800 cases, the WHO finally declares a public health emergency, for just the sixth time. Human-to-human transmission is quickly spreading and can now be found in the United States, Germany, Japan, Vietnam, and Taiwan.\n\n'
    'February 2 2020\n\nGlobal Air Travel Is Restricted by 5 pm on Sunday, those en route to the United States have to have left China or they can face a 2-week home-based quarantine if they had been in Hubei province. Mainland visitors, however, will need to undergo health screenings upon their return, and foreign nationals can even be denied admittance. Other countries beginning to impose similar air-travel restrictions at this point include Australia, Germany, Italy, and New Zealand.\n\n'
    'March 13 2020\n\nTravel Ban on Non-US Citizens Traveling From Europe Goes Into Effect the Trump administration issues a travel ban on non-Americans who visited 26 European countries within 14 days of coming to the United States. People traveling from the United Kingdom and the Republic of Ireland are exempt.\n\n'
    'March 17 2020\n\nCMS Temporarily Expands Use of Telehealth CMS expands its telehealth rules, permitting use during the COVID-19 pandemic as a means to protect older patients from potential exposure. The relaxation allows Medicare to cover telehealth visits the same as it would regular in-person visits.\n\n'
    'March 19 2020\n\nCalifornia Issues Statewide Stay-at-Home Order California becomes the first state to issue a stay-at-home order, mandating all residents to stay at home except to go to an essential job or shop for essential needs. The order also instructs health care systems to prioritize services to those who are the sickest.\n\n'
    'March 26 2020\n\nSenate Passes CARES Act the Senate passes the Coronavirus Aid, Relief, and Economic Security (CARES) Act, providing $2 trillion in aid to hospitals, small businesses, and state and local governments, while including an elimination of the Medicare sequester from May 1 through December 31, 2020.\n\n'
    'March 27 2020\n\nTrump Signs CARES Act Into Law the House of Representatives approves the CARES act, the largest economic recovery package in history, and Trump signs it into law. The bipartisan legislation provides direct payments to Americans and expansions in unemployment insurance.\n\n'
    'March 30 2020\n\nFDA Authorizes Use of Hydroxychloroquine FDA issues an emergency use authorization (EUA) for “hydroxychloroquine sulfate and chloroquine phosphate products” to be donated to the Strategic National Stockpile and donated to hospitals to treat patients with COVID-19. The EUA would be rescinded June 15, except for patients in clinical trials, in the wake of reports of heart rhythm problems among some patients.\n\n'
    'July 2 2020\n\nStates Reverse Reopening Plans several states, including California and Indiana, postpone or reverse plans to reopen their economies, as the United States records 50,000 new cases of COVID-19—the largest one-day spike since the pandemic’s onset. New Mexico also extends the state’s emergency public health order through July 15 and implements a $100 fine for those not adhering to required mask usage.\n\n'
    'July 27 2020\n\nSenate Introduces HEALS Act republicans introduce a package of bills known together as the Health, Economic Assistance, Liability Protection, and Schools (HEALS) Act, which provides provisions for another stimulus check, more money for small businesses, and liability protections for companies seeking to bring employees back to the workplace during the pandemic.\n\n'
    'August 13 2020\n\nBiden Calls for 3-Month Mask Mandate still a presidential nominee, Joe Biden calls on all governors to require their citizens to wear masks anytime they go out in public through November, and he claims he will mandate the practice if elected. At this point, there are a reported 165,000 deaths from COVID-19, and the measure is estimated to save 40,000 lives in the coming months. At this point, mask mandates still vary greatly among the states and regions.\n\n'
    'August 26 2020\n\nFDA Grants EUA to Abbott’s Rapid Test a portable rapid COVID-19 test that can deliver results in under 15 minutes was cleared by the FDA under an EUA. The test is aimed at places like workplaces and schools.\n\n'
    'September 14 2020\n\nUS Airports Stop Screening International Travelers the government announces it will stop screenings taking place at some airports since January. In March, incoming flights from high-risk countries, including China, Iran, and much of Europe, were funneled through 15 designated airports, but as of September 14, the flights will no longer be redirected and all passenger screenings will be halted. As part of the screening process, passengers had their temperatures taken and were subject to a basic health screening about typical COVID-19 symptoms before they could go through passport control and customs.\n\n'
    'September 23 2020\n\nA New, More Contagious Strain of COVID-19 Is Discovered a study conducted at Houston Methodist Hospital finds a more contagious strain of COVID-19 in a large portion of recent patient samples. Investigators analyzed samples from the earliest phase of the pandemic and a more recent infection wave, finding that nearly all strains from the more recent phase had a mutation that allows the virus to bind and infect more cells.\n\n'
    'November 16 2020\n\nFDA to Move Rapidly on EUAs for Pfizer, Moderna Vaccines on CNBC’s “Squawk Box,” HHS Secretary Alex Azar says the FDA will move “as quickly as possible” to clear Pfizer’s and Moderna’s vaccine candidates for emergency use as long as the data support authorization. Both authorization applications are currently being completed, but Azar says that the FDA’s teams are working with both companies to “remove any unnecessary bureaucratic barriers.”\n\n'
    'https://www.ajmc.com/view/a-timeline-of-covid19-developments-in-2020')
    
    #Plot Total Number of Cases
    fig7, ax7 = plt.subplots()
    ax7.bar(Months, TotCases4)
    ax7.set_xlabel('Months')
    ax7.set_ylabel('Number of Total Cases')
    ax7.set_title('USA - Total Cases Over Time')
    fig7.set_size_inches(18.5, 10.5)
    
    #Plot Daily New Cases
    fig8, ax8 = plt.subplots()
    ax8.plot(Dates, DNCases4)
    ax8.set_xlabel('February 2020 - July 2021')
    ax8.set_ylabel('Number of Daily New Cases')
    ax8.set_title('USA - Daily New Cases Over Time')
    fig8.set_size_inches(18.5, 10.5)
    plt.xticks(Dates,"")

    #generate heat map gif
    heatmapgen('USA',TotCases4,329500000,570,150,20,200)
    
    
elif cs == 'brazil':
    print('Brazil Regulation Timeline:\n\n'
    '23 March 2020 \n\nThe Federal Government published a Provisional Measure (MP) that alters a series of labor regulations during the pandemic with the aim of preserving helping companies and preserving jobs. \\nn'
    '24 March 2020 \n\nBolsonaro urges mayors and state governors to roll back lockdown measures in a televised national address. \n\n'
    '26 March 2020 \n\nThe Minister of Economy, Paulo Guedes, announced that the economic stimulus package, closed by the Ministry of Economy, Public Banks and the Central Bank will be US$ 150 billion (R$ 750 billion), to face the economic impacts of COVID-19 in Brazil. \n\n'
    '12 May 2020 \n\nBrazil’s confirmed coronavirus cases total passes Germany, as Bolsonaro tries to reopen gyms and beauty parlors by presidential decree. \n\n'
    '15 May 2020 \n\nBolsonaro loses his second health minister in less than a month after Nelson Teich resigns due to differences over the use of antimalarial drugs in treating COVID-19. \n\n'
    '18 May 2020 \n\nBrazil overtakes Britain to become the country with the third-highest number of infections, behind the United States and Russia. \n\n'
    '20 May 2020 \n\nThe Health Ministry, led by an active-duty army general on an interim basis, issues new guidelines for wider use of unproven antimalarial drugs in mild coronavirus cases. \n\n'
    '24 May 2020 \n\nU.S. limits travel from Brazil amid worsening coronavirus outbreak. \n\n'
    '6 June 2020 \n\nBrazil removes from public view months of data on its COVID-19 epidemic. “The cumulative data ... does not reflect the moment the country is in,” Bolsonaro says on Twitter. \n\n'
    '9 June 2020 \n\nBrazil restores the data following a Supreme Court ruling. \n\n'
    '12 June 2020 \n\nBrazil’s COVID-19 death toll passes Britain to become world’s second highest after the United States. \n\n'
    '19 June 2020 \n\nBrazil passes 1 million cases. two official ordinances were published in the Federal Official Gazette (DOU) to prevent, control and mitigate the risks of transmission of covid-19 in work environments. \n\n'
    'https://home.kpmg/xx/en/home/insights/2020/04/brazil-government-and-institution-measures-in-response-to-covid.html'
    'https://www.reuters.com/article/us-health-coronavirus-brazil-timeline/timeline-key-moments-in-bolsonaros-handling-of-covid-19-crisis-idINKBN2482UL'   )

    #Plot Total Number of Cases
    fig9, ax9 = plt.subplots()
    ax9.bar(Months, TotCases5)
    ax9.set_xlabel('Months')
    ax9.set_ylabel('Number of Total Cases')
    ax9.set_title('Brazil - Total Cases Over Time')
    fig9.set_size_inches(18.5, 10.5)
    
    #Plot Daily New Cases
    fig10, ax10 = plt.subplots()
    ax10.plot(Dates, DNCases5)
    ax10.set_xlabel('February 2020 - July 2021')
    ax10.set_ylabel('Number of Daily New Cases')
    ax10.set_title('Brazil - Daily New Cases Over Time')
    fig10.set_size_inches(18.5, 10.5)
    plt.xticks(Dates,"")
    #generate heat map gif
    heatmapgen('Brazil',TotCases5,212600000,775,260,20,200)
    
elif cs == 'australia':
    
    print('Australia Regulation Timeline:\n\n'
    '11 March 2020 \n\nWHO officially declares COVID-19 a pandemic \n\n'
    '12 March 2020 \n\nPrime Minister announces first economic stimulus package announced \n\n'
    'Mid-March 2020 \n\nAustralian government introduces measures to ‘slow the spread’: voluntary self-isolation of all arriving travelers, the implementation of contact tracing and expansion of testing services \n\n'
    'Mid-late March 2020 \n\nLockdown restrictions progressively implemented by Australian government to restrict citizens’ movements and reduce their opportunities to gather with other people outside their household. International and national border control measures for some states and territories introduced. Implementation of physical distancing rules \n\n'
    '20 March 2020 \n\nAustralia’s borders to all non-residents closed \n\n'
    '21 March 2020 \n\nNon-essential services and many schools closed from this date \n\n'
    '22 March 2020 \n\nSecond economic stimulus packaged announced, including changes to unemployment \n\n'
    '27 March 2020 \n\nAll returning residents required to spend two weeks in supervised quarantine \n\n'
    '29 March 2020 \n\nSafety net package to expand mental health, telehealth services, increased family violence prevention services and food provision services announced \n\n'
    '15 April 2020 \n\nJobKeeper payment legislation to support out-of-work Australians is passed \n\n'
    '26 April 2020 \n\nCOVIDSafe app, designed to help with contact tracing, is released by the federal government \n\n'
    '8 May 2020 \n\nAs the curve of cases has flattened, Australian government announces three-stage plan to begin easing lockdown restrictions \n\n'
    'Mid-May 2020 \n\nEasing of lockdown restrictions gradually introduced across Australia \n\n'
    '20 June 2020 \n\nRestrictions are reinstated in the state of Victoria as new COVID clusters begin to be recorded, in an apparent ‘second wave’ of infection \n\n'
    '4 July 2020 \n\nTwo additional postcodes are added to the Melbourne lockdown, along with nine public housing towers, whose residents were not allowed to leave the building under any circumstances \n\n'
    '7 July 2020 \n\nSecond period of lockdown is introduced for metropolitan Melbourne and Mitchell Shire after 191 new cases are recorded in those areas \n\n'
    '2 August 2020 \n\nState of disaster is declared for Victoria by Premier Andrews, including the imposition of restrictions such as a nightly curfew, mandatory face coverings in public and the closing of schools and businesses \n\n'
    '12 August 2020 \n\nRestrictions are significantly eased in Victoria, with further easing on 27 October as case numbers dwindle \n\n'
    '16 November 2020 \n\nA small outbreak of cases in Adelaide, South Australia, leads to re-impositions of restrictions and lockdown in that state and closing of borders to South Australians by Queensland, Victorian and Western Australia governments. The outbreak is quickly controlled and restrictions end on 21 November \n\n'
    '18 December 2020 \n\nThe Northern Beaches local government area of Sydney is declared a COVID hotspot due to discovery of a cluster of cases in the suburb of Avalon (total of 28 at this date), resulting in new restrictions and border controls for people living in this area and eventually Greater Sydney \n\n'
    '31 December 2020 \n\nThe year ends with NSW recording ten new community acquired cases (reaching a total of 144 cases in the Avalon cluster) and Melbourne community acquired cases reaching a total of eight. In response, the Victorian government re-imposes some restrictions in the state, including mandatory mask wearing when inside public places and closing the border with the entire state of NSW again. Western Australia re-introduces a hard border with both Victoria and NSW, while South Australia closes its border to NSW. Household visitors across Greater Sydney are limited to five people and no-one is allowed into Sydney Central Business District on New Year’s Eve. The traditional Sydney Harbour fireworks display goes ahead without crowds viewing them \n\n'
    '31 December 2020 \n\nBy this date, Australia has recorded a total of 28,381 COVID cases and 909 deaths. The most affected state by far is Victoria, with 20,365 cases and 820 deaths, followed by NSW with 4,906 cases and 54 deaths, Queensland with 1,250 cases and 6 deaths, Western Australia with 859 cases and 9 deaths, South Australia with 575 cases and 4 deaths, the Australian Capital Territory with 118 cases and 3 deaths and the Northern Territory with 74 cases and 0 deaths \n\n'
    'https://deborahalupton.medium.com/timeline-of-covid-19-in-australia-1f7df6ca5f23')
    
    #Plot Total Number of Cases
    fig11, ax11 = plt.subplots()
    ax11.bar(Months, TotCases6)
    ax11.set_xlabel('Months')
    ax11.set_ylabel('Number of Total Cases')
    ax11.set_title('Australia - Total Cases Over Time')
    fig11.set_size_inches(18.5, 10.5)
    
    #Plot Daily New Cases
    fig12, ax12 = plt.subplots()
    ax12.plot(Dates, DNCases6)
    ax12.set_xlabel('February 2020 - July 2021')
    ax12.set_ylabel('Number of Daily New Cases')
    ax12.set_title('Australia - Daily New Cases Over Time')
    fig12.set_size_inches(18.5, 10.5)
    plt.xticks(Dates,"")

    #generate heat map gif
    heatmapgen('Australia',TotCases6,25690000,40,250,20,200)