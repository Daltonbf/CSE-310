%% calculator.erl
%% This module implements a basic calculator in Erlang.
-module(calculator).
-export([start/0, calculate/1, perform_operation/2, test/0]).

%% Start a new calculator process.
start() ->
    spawn(fun() -> process() end).

%% Process function to handle incoming messages.
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

%% Calculate function to perform arithmetic operations.
calculate(add, Num1, Num2) ->
    %% Add two numbers.
    Num1 + Num2;
calculate(sub, Num1, Num2) ->
    %% Subtract two numbers.
    Num1 - Num2;
calculate(mul, Num1, Num2) ->
    %% Multiply two numbers.
    Num1 * Num2;
calculate(div, Num1, 0) ->
    %% Handle division by zero.
    throw(division_by_zero);
calculate(div, Num1, Num2) ->
    %% Divide two numbers.
    Num1 / Num2;
calculate(mod, Num1, Num2) ->
    %% Calculate the modulus of two numbers.
    Num1 rem Num2;
calculate(pow, Num1, Num2) ->
    %% Calculate the power of two numbers.
    math:pow(Num1, Num2).

%% Perform an operation on a list of number pairs.
perform_operation(Operation, NumList) ->
    %% Use lists:map and a lambda function to apply the operation to each pair.
    lists:map(fun({Num1, Num2}) -> calculate(Operation, Num1, Num2) end, NumList).

%% Test the calculator.
test() ->
    CalculatorPid = start(),
    CalculatorPid! {add, 10, 5},
    CalculatorPid! {sub, 10, 5},
    CalculatorPid! {mul, 10, 5},
    CalculatorPid! {div, 10, 5},
    CalculatorPid! {div, 10, 0},
    CalculatorPid! {mod, 10, 3},
    CalculatorPid! {pow, 2, 3},
    NumList = [{1, 2}, {3, 4}, {5, 6}],
    io:format("Results: ~p~n", [perform_operation(add, NumList)]),
    io:format("Results: ~p~n", [perform_operation(sub, NumList)]),
    io:format("Results: ~p~n", [perform_operation(mul, NumList)]),
    io:format("Results: ~p~n", [perform_operation(div, NumList)]),
    io:format("Results: ~p~n", [perform_operation(mod, NumList)]),
    io:format("Results: ~p~n", [perform_operation(pow, NumList)]),
    timer:sleep(1000),
    exit(CalculatorPid, kill).

%% Run the test.
test().