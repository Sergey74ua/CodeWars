// Deodorant Evaporator

unit Kata;

interface

function Evaporator(content, evapPerDay, threshold: Double): Int64;

implementation

uses Math;

function Evaporator(content, evapPerDay, threshold: Double): Int64;
    begin
        Result := 0;
        threshold := content * (threshold / 100);
        evapPerDay := 1 - evapPerDay / 100;
        while content > threshold do
        begin
          content := content * evapPerDay;
          Result := Result + 1;
        end;
    end;

end.
