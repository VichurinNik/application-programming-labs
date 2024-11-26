from parser import parser
from dataframe import *


def main():
    args = parser()
    try:
        df=create_dataframe(args.annotation_file)
        print("DataFrame создан:")
        print(df)
        add_image(df)
        print("Размеры изображений:")
        dk = df.take([2, 3, 4], axis=1)
        print(dk)
        print("Статистика изображений:")
        print(image_statistics(df))
        print("Изображения после фильтрации по размеру:")
        print(filter_images_by_size(df,args.max_width,args.max_height))
        df=add_area_column(df)
        print("Колонка с площадью добавлена:")
        print(df)
        df=sort_by_area(df)
        print("DataFrame отсортирован по площади:")
        print(df)
        plot_column_distribution(df["Area"], 'Площадь')
    except Exception as e:
        print('Error: ', e)


if __name__ == '__main__':
    main()