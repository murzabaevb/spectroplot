from spectroplot import SpectrumPlotter

plotter = SpectrumPlotter(excel_file='data.xlsx')
plotter.load_data()
plotter.plot(min_freq=860, max_freq=960)
