function show_hybrid(im)

subplot(3,4,[1 11])
imagesc(im), axis image
set(gca,'xcolor','w','ycolor','w','xtick',[],'ytick',[])
subplot(3,4,4)
imagesc(im), axis image
set(gca,'xcolor','w','ycolor','w','xtick',[],'ytick',[])

end