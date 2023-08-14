# dateiter

Simple date iterator tool.

## Usage
```sh
for date in $(dateiter 2020-01-01 2020-01-05); do
    echo $date
done

# 2020-01-01
# 2020-01-02
# 2020-01-03
# 2020-01-04
```
