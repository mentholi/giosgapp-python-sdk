# giosgapp-python-sdk
Unofficial python SDK for GiosgApps. This is working in progress and should not be used just yet!


## Usage example
```python

In [1]: from giosgappsdk import GiosgAppSDK

In [2]: secret = 'b816304c420db33a33b276d1a275f580236c15da'

In [3]: url = 'https://foobar.io/app/?type=manual_nav&data=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2loiNmQzMjkwMDAtOWJkZi0xMWU0LWE2ZjgtNmM0MDA4YWRmN2U4Iiwic3ViIjoiMTI3LjAuMC4xOjgwMDAiLCJleHAiOjE0NDc3MTA2ODIsInZpc2l0b3JfaWQiOiIiLCJfb3JnX2lkIjoxLCJpbnN0X2lkIjoiZjk0M2RkMDItNmRkMi0xMWU1LTk0YTItNmM0MDA4YWRmN2U4Iiwib3JnX2lkIjoiNmQzMjkwMDAtOWJkZi0xMWU0LWJkMTEtNmM0MDA4YWRmN2U4IiwiYXBwX2lkIjoiZjZhYWE0MjYtNmRkMi0xMWU1LWEzYzUtNmM0MDA4YWRmN2U4IiwiX3VzZXJfaWQiOjEsImNoYXRfaWQiOiIifQ._SZmqFZdOha4Qdlk0nykUozqOViMtRnUhowbqmwuyMs&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNmQzMjkwMDAtOWJkZi0xMWU0LWE2ZjgtNmM0MDA4YWRmN2U4Iiwic3ViIjoiMTI3LjAuMC4xOjgwMDAiLCJwZXJtcyI6W10sIm9yZ19pZCI6IjZkMzI5MDAwLTliZGYtMTFlNC1iZDExLTZjNDAwOGFkZjdlOCIsImFwcF9pZCI6ImY2YWFhNDI2LTZkZDItMTFlNS1hM2M1LTZjNDAwOGFkZjdlOCIsImluc3RfaWQiOiJmOTQzZGQwMi02ZGQyLTExZThMi02YzQwMDhhZGY3ZTgiLCJleHAiOjE0NDc3MTA2ODJ9.T7vqRivaG-terVCc4bBcikdcHxt0dsjvd1Yn_U_Thz0'

In [4]: sdk = GiosgAppSDK(url, secret)

In [5]: sdk.get_users()
Out[5]: <Response [200]> # Do something with the response
```