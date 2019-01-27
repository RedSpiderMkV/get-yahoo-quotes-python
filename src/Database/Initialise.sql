CREATE DATABASE YahooHistoricData;

USE YahooHistoricData;

CREATE TABLE QuoteSymbol(
Id int auto_increment not null,
Ticker varchar(10),
Name varchar(255),
primary key (Id)
);

CREATE TABLE QuoteData(
SymbolId int not null,
RetrieveDate DateTime,
QuoteDate Date,
Open decimal,
High decimal,
Low decimal,
Close decimal,
Volume decimal,
primary key (SymbolId, QuoteDate),
foreign key (SymbolId) references QuoteSymbol(Id)
);
