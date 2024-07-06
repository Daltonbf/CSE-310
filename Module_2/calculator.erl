-module(calculator).
-export([start/0, calculate/1]).

start() ->
    spawn(fun() -> process() end).

process() ->
    receive
        {Operation, Num1, Num2} ->
            Result = calculate(Operation, Num1, Num2),
            io:format("Result: ~p~n", [Result]),
            process();
        _ ->
            io:format("Invalid operation~n"),
            process()
    end.

calculate(add, Num1, Num2) -> Num1 + Num2;
calculate(sub, Num1, Num2) -> Num1 - Num2;
calculate(mul, Num1, Num2) -> Num1 * Num2;
calculate(div, Num1, 0) -> throw(division_by_zero);
calculate(div, Num1, Num2) -> Num1 / Num2.

perform_operation(Operation, NumList) ->
    lists:map(fun({Num1, Num2}) -> calculate(Operation, Num1, Num2) end, NumList).

test() ->
    CalculatorPid = start(),
    CalculatorPid! {add, 10, 5},
    CalculatorPid! {sub, 10, 5},
    CalculatorPid! {mul, 10, 5},
    CalculatorPid! {div, 10, 5},
    CalculatorPid! {div, 10, 0},
    NumList = [{1, 2}, {3, 4}, {5, 6}],
    io:format("Results: ~p~n", [perform_operation(add, NumList)]),
    io:format("Results: ~p~n", [perform_operation(sub, NumList)]),
    io:format("Results: ~p~n", [perform_operation(mul, NumList)]),
    io:format("Results: ~p~n", [perform_operation(div, NumList)]).