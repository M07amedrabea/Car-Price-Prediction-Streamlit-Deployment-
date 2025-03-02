# Import Libraries

import streamlit as st
import pandas as pd
import pickle

# Upload Data

data = pickle.load(open(r'C:\Users\HP\Desktop\Car Price Prediction Challenge\model1.sav','rb'))

# streamlit page 

st.title('Car Price Prediction')
st.sidebar.header('Feature Selecting')
st.sidebar.info('Easy App for prediction Cares Price')

st.image('https://www.topgear.com/sites/default/files/images/news-article/carousel/2018/11/4c16571ee0d81e04b092beabd12d56e6/526140.jpg')

cars_names = ['LEXUS', 'CHEVROLET', 'HONDA', 'FORD', 'HYUNDAI', 'TOYOTA',
       'MERCEDES-BENZ', 'OPEL', 'PORSCHE', 'BMW', 'JEEP', 'VOLKSWAGEN',
       'AUDI', 'RENAULT', 'NISSAN', 'SUBARU', 'DAEWOO', 'KIA',
       'MITSUBISHI', 'SSANGYONG', 'MAZDA', 'GMC', 'FIAT', 'INFINITI',
       'ALFA ROMEO', 'SUZUKI', 'ACURA', 'LINCOLN', 'VAZ', 'GAZ',
       'CITROEN', 'LAND ROVER', 'MINI', 'DODGE', 'CHRYSLER', 'JAGUAR',
       'ISUZU', 'SKODA', 'DAIHATSU', 'BUICK', 'TESLA', 'CADILLAC',
       'PEUGEOT', 'BENTLEY', 'VOLVO', 'სხვა', 'HAVAL', 'HUMMER', 'SCION',
       'UAZ', 'MERCURY', 'ZAZ', 'ROVER', 'SEAT', 'LANCIA', 'MOSKVICH',
       'MASERATI', 'FERRARI', 'SAAB', 'LAMBORGHINI', 'ROLLS-ROYCE',
       'PONTIAC', 'SATURN', 'ASTON MARTIN', 'GREATWALL']
N_Cars_names = [16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 23, 20,  0, 44, 19, 39,  7, 25,  4,
       33, 47, 15,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]

Manufacturer_Mapping = dict(zip(cars_names,N_Cars_names))
Manufacturer1 = st.selectbox('Manufacturer',cars_names)
Manufacturer2 = Manufacturer_Mapping[Manufacturer1]
#----------------------------------------------------------------------------------------------------

Model_names = ['RX 450', 'Equinox', 'FIT', ..., 'E 230 124', 'RX 450 F SPORT',
       'Prius C aqua']
N_Model_names = [347, 334, 683, 616, 697, 194, 167, 313, 294, 430, 469, 623,  99,
       336, 226, 545, 300, 484, 273, 397, 776,  66, 770, 213, 556, 836,
       269, 577, 383, 504,  37, 416, 725, 377, 611,  94, 499,  63, 689,
       652, 812, 743, 445,  40, 328,  67, 660, 217,   2, 145, 810, 758,
       778, 746, 344, 447, 427, 175, 784, 657, 694, 595, 119, 223, 184,
       112, 245, 672, 411, 691, 751, 152,  91, 676, 654, 304, 263, 118,
       523, 232, 581, 199, 525, 461,  98, 798, 414, 231, 153, 658, 407,
       124, 104, 571, 692, 509, 332, 808,  80, 497,  30, 329, 158, 821,
       661, 109, 249, 171, 371, 239, 235,  74, 254, 649, 570, 501, 462,
       374, 534, 537, 686,  25, 559, 720, 529, 437, 709, 323, 117, 308,
       680,  51, 279, 258, 246, 673,  83, 648,  86, 428, 444, 285, 185,
        89, 406, 393, 468, 238, 761, 833, 105, 549, 636, 717,   3, 306,
       721, 792, 366, 216, 737, 284, 739, 744,  73, 846, 450, 275, 452,
         8, 760, 582, 612, 224, 841,  16, 832, 207, 500, 567, 538, 466,
       454, 753, 688, 394, 696,  69, 481, 251,  36, 831, 763, 326, 198,
       365, 467, 243, 557, 265,  65, 188, 698, 137, 706, 127, 222, 512,
       589, 711, 139, 735, 780, 227, 395, 796, 521, 281, 259, 754, 741,
       816, 436, 179, 578, 116, 749, 203, 353, 795, 422,   7, 517, 592,
        97, 233,  77, 712, 221, 420, 429, 364, 789, 664, 835, 613, 252,
       286, 471, 565, 182, 141, 292, 747, 409,  42, 168,  12,  81, 540,
       391, 338, 453, 201, 456, 457, 443, 277, 230, 584,  53, 669,  11,
       351, 434, 165, 543, 190, 142,  28, 417, 164, 135, 681,   9,  45,
       425, 209, 439, 289, 828, 333, 583, 598, 204, 342,  82,  95, 387,
       585, 690, 524, 242, 765, 154, 330, 759, 186, 189, 106, 320, 114,
       558, 548, 824, 318, 278, 522, 163, 628, 255, 700, 637, 663, 474,
       121, 380,  85, 390,  90,  49, 745, 103, 684, 727, 586, 804,  62,
       123, 701, 644, 662, 622, 615, 837,  59, 550, 418,  50, 331, 544,
       352, 324, 379, 211, 715, 272, 195, 180, 506, 197,  61, 177, 505,
       322, 677, 659,  26,  31, 458, 368, 600, 845, 316, 120, 756, 256,
       781, 820, 298, 261, 287,  41, 819, 809,  43,  93, 465, 268, 280,
       566, 125, 687,  71, 671, 413, 271, 157, 101, 405,  33, 719, 250,
       493,  92, 554, 441, 704, 196, 498, 825, 527, 376, 449, 848, 645,
       183, 311, 785, 764, 842, 617, 228, 476, 572,  60, 702, 790, 495,
       827, 840, 375, 100, 742, 608, 291,  17, 757, 762, 369, 791, 210,
       442, 170, 206, 766, 646, 337, 237, 102, 340, 847, 562, 301, 655,
       783, 172, 528,  23, 310, 360, 514, 435, 635, 244, 162, 319,  72,
         1, 381, 634, 811, 656, 555, 607, 151, 603, 302, 478,  52, 826,
        14, 382, 362, 147, 625, 160, 818, 496, 192,  39, 665, 220, 173,
       155, 388, 593, 270, 771, 455, 248, 218, 752, 283, 290,  75, 569,
       531,  47, 473, 361,  46, 161, 143, 426,   0, 438, 225, 234, 599,
       303, 588, 260, 639, 526, 208, 314, 136, 767, 769, 126, 156, 341,
       288, 451, 181, 813, 392, 384, 488, 507,  84, 621, 530,  24, 487,
       346, 510, 829, 363, 385, 580, 174, 148, 573, 299, 389, 149, 122,
       516, 138, 838,   4, 724, 823, 643, 668, 705, 773, 729, 214, 596,
       475, 396, 699, 560, 503, 166, 619, 345, 400, 519,   5, 822, 511,
       787, 814, 803, 606, 710, 535, 614, 679, 536, 312,  10, 642, 653,
       115,  70, 370, 640, 678, 421,  58, 399, 722, 561, 736, 356, 419,
       666, 111, 631, 564, 542, 718, 202, 748, 401, 732, 553, 349, 424,
       494, 513, 219, 730,  21,  27,  54, 774, 716, 772, 432, 723, 740,
       552, 547, 480, 257, 412, 733, 276, 587, 348, 372, 431, 755, 264,
       682,  55, 650,  88, 262, 728,  29, 483, 307, 367, 532, 807, 777,
       801, 602, 667, 817, 309, 398, 768, 215, 315, 267, 786,  78, 108,
       788,  76, 491, 797, 335,  56, 800, 849, 597, 834, 321,  32, 144,
       651, 113,  34, 482, 159,  20, 131, 782, 169, 440, 590,  64, 626,
       463, 609, 193, 296, 731, 350, 568, 479, 132, 325, 779, 632, 282,
       305,  57, 541, 520, 446, 533,  18, 107,  96, 459, 830, 408, 799,
        15, 726, 734, 839,   6,  19, 176, 236, 604, 130, 685, 575, 713,
       802, 708, 618, 433,  87, 253, 539, 150, 563, 128, 133,  13, 695,
       518, 295, 703, 146, 546, 502, 297, 674, 670, 630, 490, 354, 485,
       415, 775, 191,  35, 205,  48, 129, 402, 266, 815, 359, 317, 601,
       404, 605, 187, 591, 675, 551, 843, 641, 647, 620, 134, 212, 200,
        38, 489, 844, 794, 633, 358, 508, 693, 486, 477, 240, 293, 423,
       464, 460, 247, 241, 274, 110, 738, 515, 472, 357, 229, 470, 386,
       707, 373, 448, 339,  22, 627, 714, 750,  44, 629,  68, 178, 594,
       624, 574, 410, 610, 492,  79, 638, 140, 378, 576, 579, 327, 403,
       793, 805, 806, 355, 343]
Model_Mapping = dict(zip(Model_names,N_Model_names))
Model1 = st.selectbox('Model',Model_names)  
Model2 = Model_Mapping[Model1]

#----------------------------------------------------------------------------------------------------

Category_names = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon',
       'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine',
       'Pickup']

N_Category_names = [3, 4, 8, 9, 6, 0, 1, 5, 2, 7]

Category_Mapping = dict(zip(Category_names,N_Category_names))

Category1 = st.selectbox('Category',Category_names) 
Category2 = Category_Mapping[Category1]

#----------------------------------------------------------------------------------------------------

Leather_interior = ['Yes', 'No']

N_Leather_interior = [1,2]

Leather_interior_Mapping = dict(zip(Leather_interior,N_Leather_interior))

Leather_interior1 = st.selectbox('Leather_interior',Leather_interior)
Leather_interior2 = Leather_interior_Mapping[Leather_interior1]

#----------------------------------------------------------------------------------------------------

fuel_type =['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG','Hydrogen']
N_fuel_type = [4, 2, 1, 5, 3, 0, 6]

fuel_type_Mapping = dict(zip(fuel_type,N_fuel_type))

fuel_type1 = st.selectbox('fuel_type',fuel_type)

fuel_type2 = fuel_type_Mapping[fuel_type1]

#----------------------------------------------------------------------------------------------------

Color =['Silver', 'Black', 'White', 'Grey', 'Blue', 'Green', 'Red',
       'Sky blue', 'Orange', 'Yellow', 'Brown', 'Golden', 'Beige',
       'Carnelian red', 'Purple', 'Pink']
N_Color = [ 1, 14, 12,  7,  2, 13, 11,  8,  6, 15,  3,  5,  0,  4, 10,  9]

Color_Mapping = dict(zip(Color,N_Color))

Color1 = st.selectbox('Color',Color)

Color2 = Color_Mapping[Color1]

#----------------------------------------------------------------------------------------------------

Wheel =['Left wheel', 'Right-hand drive']
N_Wheel = [1, 0]

Wheel_Mapping = dict(zip(Wheel,N_Wheel))

Wheel1 = st.selectbox('Wheel',Wheel)

Wheel2 = Wheel_Mapping[Wheel1]

#----------------------------------------------------------------------------------------------------

Drive_wheels = ['4x4', 'Front', 'Rear']
N_Drive_wheels = [1, 0, 2]

Drive_wheels_Mapping = dict(zip(Drive_wheels,N_Drive_wheels))

Drive_wheels1 = st.selectbox('Drive_wheels',Drive_wheels)

Drive_wheels2 = Drive_wheels_Mapping[Drive_wheels1]

#----------------------------------------------------------------------------------------------------

Gear_box_type = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
N_Gear_box_type = [3, 0, 2, 1]

Gear_box_type_Mapping = dict(zip(Gear_box_type,N_Gear_box_type))

Gear_box_type1 = st.selectbox('Gear_box_type',Gear_box_type)

Gear_box_type2 = Gear_box_type_Mapping[Gear_box_type1]

#----------------------------------------------------------------------------------------------------

Engine_volume = st.selectbox('Engine volume',[1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
       1.9, 2.7, 3.5, 2.1, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1])

#----------------------------------------------------------------------------------------------------

Airbags = st.selectbox('Airbags',[ 2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13])


#----------------------------------------------------------------------------------------------------

Car_Age = st.number_input('Car_Age')

#----------------------------------------------------------------------------------------------------

Milage = st.number_input('Milage')

#----------------------------------------------------------------------------------------------------

N_Levy = [  0, 293, 170, 306, 266, 263, 155,  20, 282, 197, 210,  48, 207,
       250,  85,  22, 232, 154, 188,   3, 221, 274, 196, 226, 268, 271,
       272, 317, 269, 230,  39, 286, 225,  31, 265, 228,  24, 322, 177,
       327, 240, 291,  71, 139, 214, 247, 209, 180, 241, 145,  74,  19,
       208, 287,  38, 307,  49, 171, 254, 187, 148,  66, 137, 256, 181,
        57,  15, 173, 303, 308, 279,  55, 169,  12, 277,  11, 195, 205,
       141,  84, 102,  76,  21, 211,  50, 301, 227, 261, 150, 300,  46,
        34, 156, 275,   5,  73, 313,  82, 264, 224, 184, 167, 203, 289,
       183, 326,  99, 179,  25, 324, 310,  51, 314, 270, 231, 198, 213,
       328, 281, 323,  53,  64, 118, 244, 176, 161, 149,  89, 126, 253,
       174, 299, 309, 273, 172,  35, 290,  54,  67, 252, 305, 246, 108,
       189, 276, 190,  60,  26, 201, 292, 251, 202, 186,  43, 242, 160,
       113,  78, 182, 152, 127, 191,  59,  77,  93, 312, 220, 249, 158,
       304, 106, 319, 132, 168, 258, 216, 112,  65,  17, 162, 233, 140,
       124,  40,   8, 329, 135, 185, 165, 320, 131,  94, 114, 267,  14,
       217, 133, 219, 115,   2, 259,  58,  32, 325, 136,  45,  41,  33,
       248, 121, 318, 234, 153,  69, 130, 257,  44, 245,  63, 143, 164,
        90,  95,  36, 129, 280,  87, 199, 111,  62, 157,  61, 193, 239,
        28,  83,  47,  18, 200, 120,  70, 255, 243, 206, 163, 151, 119,
        96,  72, 237, 109, 134, 107, 315, 284, 288, 194,  68, 100,  13,
       285, 144,  91,   4,  16,  88, 204,  81,  56,  30, 166, 142, 235,
       178, 260, 229, 238,  80, 311, 302, 146,  92,  97,   6,  23, 159,
        75, 297,  29, 296,  37, 122,   1, 104, 316, 116, 321, 175, 212,
       125,  52, 262, 192, 101, 236, 215, 147,  27,  79, 105, 110, 218,
       283, 294,   7,   9, 123, 278, 222, 138, 223, 103, 128, 295, 117,
        42,  10,  98, 298,  86]



Levy = st.selectbox('Levy',N_Levy)


#----------------------------------------------------------------------------------------------------

Cylinders = st.number_input('Cylinders')

#----------------------------------------------------------------------------------------------------

df = pd.DataFrame({'Levy':Levy,'Manufacturer':Manufacturer2,'Model':Model2,'Category':Category2,'Leather interior':Leather_interior2,'Fuel type':fuel_type2,
'Mileage':Milage,'Gear box type':Gear_box_type2,'Drive wheels':Drive_wheels2,'Wheel':Wheel2,
'Color':Color2,'Engine volume':Engine_volume,'Cylinders':Cylinders,'Airbags':Airbags,'Car_age':Car_Age},index=[0])

b = st.sidebar.button('Predict Price')

if b:
    pre = data.predict(df)
    st.sidebar.write('Price is : ',pre)



