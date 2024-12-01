clc
close all
clearvars

data = sort(load("bigboy_day1.txt"));
silver = sum(abs(data(:,1)-data(:,2)))

counts = zeros(max(data(:)),1);
for i = 1:length(data(:,1))
    counts(data(i,2)) = counts(data(i,2)) + 1;
end
gold = sum(data(:,1).*counts(data(:,1)))