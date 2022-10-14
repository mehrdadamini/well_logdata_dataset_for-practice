
def wellLogdisply(df):
    from matplotlib.pyplot import figure
    import matplotlib.pyplot as plt

    figure(figsize=(30,15))

    plt.subplot(161)
    plt.title('ILD_log10')
    plt.xlim(df['ILD_log10'].min()-10,df['ILD_log10'].max()+10)
    plt.plot(df["ILD_log10"].values, df['Depth'].values,'r', lw=2)

    plt.subplot(162)
    plt.title('GR')
    plt.xlim(df['GR'].min()-10,df['GR'].max()+10)
    plt.plot(df["GR"].values, df['Depth'].values, lw=2)

    plt.subplot(163)
    plt.title('DeltaPHI')
    plt.xlim(df['DeltaPHI'].min()-10,df['DeltaPHI'].max()+10)
    plt.plot(df["DeltaPHI"].values, df['Depth'].values, 'g', lw=2)

    plt.subplot(164)
    plt.title('PHIND')
    plt.xlim(df['PHIND'].min()-10,df['PHIND'].max()+10)
    plt.plot(df["PHIND"].values, df['Depth'].values, 'c', lw=2)

    plt.subplot(165)
    plt.title('PE')
    plt.xlim(df['PE'].min()-10,df['PE'].max()+10)
    plt.plot(df["PE"].values, df['Depth'].values, 'b',lw=2)

    plt.subplot(166)
    plt.title('RELPOS')
    plt.xlim(df['RELPOS'].min()-10,df['RELPOS'].max()+10)
    plt.plot(df["RELPOS"].values, df['Depth'].values, 'm',lw=2)


    return plt.show()
    